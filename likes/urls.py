from django.urls import path
from . import views

urlpatterns = [
    path('<int:post>/', views.LikeDetail.as_view(), name='likes'), 
]