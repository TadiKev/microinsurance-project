# backend/users/views.py
from rest_framework import viewsets, permissions, generics
from .models import User
from .serializers import UserSerializer, RegisterSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only list/detail of users (for admin / underwriters as needed).
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
