from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('verify_email/', verify_email, name='verify_email'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]