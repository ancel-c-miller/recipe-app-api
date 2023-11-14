"""
User Views
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create an new user in system"""
    serializer_class = UserSerializer
