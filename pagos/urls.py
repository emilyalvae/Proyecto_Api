from rest_framework.routers import DefaultRouter
from .views import ServiceView,PaymentUserView, ExpiredPaymentView

pagos_router = DefaultRouter()

pagos_router.register(r"v2/service", ServiceView, basename= "service_viewset")
pagos_router.register(r"v2/payment", PaymentUserView, basename= "payment_viewset")
pagos_router.register(r"v2/expired", ExpiredPaymentView, basename= "expired_viewset")
urlpatterns = pagos_router.urls