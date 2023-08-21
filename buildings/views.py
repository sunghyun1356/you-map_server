from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from .serializers import *
from .models import BuildingPurpose, Building
from .permissions import IsOwnerOrReadOnly

# 빌딩 목록 반환
class BuildingAPIViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes =[AllowAny]
    

