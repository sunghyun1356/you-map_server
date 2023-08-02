from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .serializers import *
from .models import BuildingPurpose, Building

# 빌딩 목록 반환
class BuildingAPIViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    

