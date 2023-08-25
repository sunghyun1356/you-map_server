from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
import random
from rest_framework import generics
from .serializers import *

from .models import validate_email_domain
from .models import MyUser

import json
User = get_user_model()

def generate_verification_code():
    return str(random.randint(100000, 999999))

def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        nickname = data.get('nickname')
        school = data.get('school')

        try:
            validate_email(email)  # 이메일 형식 검증
            validate_email_domain(email)  # 도메인 검증
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)

        if email and password and name and nickname and school:
            # 인증 코드 생성 및 저장
            verification_code = generate_verification_code()
            user = User.objects.create_user(email=email, password=password, name=name, nickname=nickname, school=school, verification_code=verification_code)

            # 인증 메일 전송
            send_mail(
                'Email Verification',
                f'Your verification code is: {verification_code}',
                'soganglikelionverify@gmail.com',
                [email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Verification code sent to your email. Please check your email and complete the registration.'})
        return JsonResponse({'message': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
@csrf_exempt
def verify_email(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        verification_code = data.get('verification_code')

        try:
            user = User.objects.get(email=email, verification_code=verification_code)
            user.is_email_verified = True
            user.save()
            return JsonResponse({'message': 'Email verification successful. You can now complete the registration.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid verification code'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': "Login Success!"})
        else:
            messages.error(request, '이메일이나 비밀번호가 잘못되었습니다.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    messages.info(request, '로그아웃 되었습니다.')
    return JsonResponse({"message" : "Logout Success!"},status=status.HTTP_201_CREATED)

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class CustomTokenOBtainPairAPIView(TokenObtainPairView):
    pass