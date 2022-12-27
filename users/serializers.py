from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email", "password"]
        
    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("El email ya ha sido usado")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)

        return user
    
class GetUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email", "password"]