from django.db import models
from django.contrib.auth.models import AbstractUser
from content.models import ContentModel


class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user" # 여기는 테이블 이름입니다

    nickname = models.CharField(unique=True, max_length=20)
    wishList = models.ManyToManyField('content.ContentModel', related_name="wishList", default=None, blank=True)

class WishList(models.Model):

    class Meta:
        db_table = "wishlists"

    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE)
    content = models.ForeignKey('content.ContentModel', on_delete=models.CASCADE)