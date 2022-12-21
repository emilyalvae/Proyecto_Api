from rest_framework.serializers import ModelSerializer
from .models import Service, PaymentUser, ExpiredPayment

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class PaymentUserSerializer(ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = "__all__"

class ExpiredSerializer(ModelSerializer):
    class Meta:
        model = ExpiredPayment
        fields = "__all__"
        