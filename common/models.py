from django.db import models
from django.contrib.auth.models import AbstractUser #사용자 user 모델 추가

class Member_info(AbstractUser):
    member_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    zipcode = models.CharField(max_length=10)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)