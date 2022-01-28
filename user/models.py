from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user" # 여기는 테이블 이름입니다

    nickname = models.CharField(unique=True, max_length=20)