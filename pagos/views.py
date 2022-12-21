from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet
from .serializers import ServiceSerializer,PaymentUserSerializer,ExpiredSerializer
from .models import Service, PaymentUser, ExpiredPayment
from rest_framework import mixins
from .pagination import SimplePagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle

class ServiceView(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    throttle_scope = 'get'

class PaymentUserView(ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    pagination_class = SimplePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["payment_date", "expiration_date"]
    throttle_scope = 'get_pagos'

class ExpiredPaymentView(mixins.CreateModelMixin,mixins.ListModelMixin,GenericViewSet):
    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredSerializer
    throttle_scope = 'get'