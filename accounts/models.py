from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models

#서강 이메일 주소만 허용
def validate_email_domain(value):
    valid_domains = ['sogang.ac.kr']
    email = value.split('@')
    if len(email) == 2 and email[1] in valid_domains:
        return True
    raise ValidationError("서강대학교 도메인 주소를 통한 이메일 인증만 가능합니다.")

#사용자 모델 관리
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('올바른 이메일 주소를 입력하세요.')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email=email, password=password, **extra_fields)

class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True, validators=[validate_email_domain])
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50, null=False)
    nickname = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    is_email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['name', 'nickname']