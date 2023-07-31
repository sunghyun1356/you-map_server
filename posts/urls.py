from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('popular/', views.PurposeListView.as_view(), kwargs={'ordering': 'popular'}), 
    path('recent/', views.PurposeListView.as_view(), kwargs={'ordering': 'recent'}), 
]