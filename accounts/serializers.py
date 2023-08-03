from rest_framework import serializers

from .models import *

class WriterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ['nickname']
        
class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

