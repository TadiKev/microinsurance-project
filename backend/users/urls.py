# backend/users/urls.py
from rest_framework import routers
from .views import UserViewSet, RegisterAPIView
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
]
