from rest_framework.routers import DefaultRouter
from .api import UserViewSet

user_router = DefaultRouter()

user_router.register(r'users', UserViewSet,basename = "users")

urlpatterns = user_router.urls