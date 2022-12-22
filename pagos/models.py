from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="logo", null=True) #(upload_to="logo",null=True)

    class Meta:
        db_table = "servicio"

    def __str__(self):
        return self.name

class PaymentUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service,on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    
    class Meta:
        db_table = "pago"

    def __str__(self):
        return self.amount

class ExpiredPayment(models.Model):
    pay_user_id = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField()

    class Meta:
        db_table = "pago expirado"
    
    def __str__(self):
        return self.penalty_fee_amount