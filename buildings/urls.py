from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', BuildingListAPIView.as_view({'get': 'list'})),
    path('<int:pk>',BuildingListAPIView.as_view({'get':'retrieve'}) ),

    
]

