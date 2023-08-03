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

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user

