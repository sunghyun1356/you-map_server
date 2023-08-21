from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', BuildingAPIViewSet.as_view({'get': 'list'})),
    path('<int:pk>',BuildingAPIViewSet.as_view({'get':'retrieve'}) ),

    
]

