from rest_framework import serializers
from .models import MyUser

class WriterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ['nickname']