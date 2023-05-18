from rest_framework import generics

from . import models
from . import serializers


class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
