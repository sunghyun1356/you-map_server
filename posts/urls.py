from django.contrib import admin
from django.urls import path

from . import views
from likes import views as like_views

urlpatterns = [
    path('popular/', views.PurposeListView.as_view(), kwargs={'ordering': 'popular'}), 
    path('recent/', views.PurposeListView.as_view(), kwargs={'ordering': 'recent'}),
    path('<int:pk>', views.PostDetailAPIView.as_view()),
    path('<int:post>/like/', like_views.LikeDetail.as_view()), 
    path('', views.PostListAPIView.as_view()),
    path('create/',views.PostCreateAPIView.as_view()),
]