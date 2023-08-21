from django.contrib import admin
from django.urls import path

from . import views
from likes import views as like_views

urlpatterns = [
    path('popular', views.PopularFirstPostListAPIView.as_view()),
    path('recent', views.RecentFirstPostListAPIView.as_view()),
    path('<int:pk>', views.PostDetailAPIView.as_view()),
    path('',views.PostCreateAPIView.as_view()),

]