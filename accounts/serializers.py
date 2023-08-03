from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

class UserBaseSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields ='__all__'