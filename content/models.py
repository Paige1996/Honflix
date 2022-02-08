import ast
import json

from django.db import models


class Category(models.Model):

    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=50)



class ContentModel(models.Model):

    class Meta:
        db_table = "content"

    title = models.CharField(max_length=100)
    description = models.TextField()
    video_similar = models.URLField(max_length=2000)
    thumbnailURL = models.URLField(max_length=2000)
    videoURL = models.URLField(max_length=2000)
    categories = models.ForeignKey('content.Category', related_name="categories", on_delete=models.CASCADE)

    def set_video_similar(self, x):
        self.video_similar = json.dumps(x)

    def get_video_similar(self):
        return ast.literal_eval(json.loads(self.video_similar))
    # related_name :어떻게 찾기를 원하는가. 카테고리를 찾을때 이름.

    # "Class_name" = 클래스 이름. Q ""와 그냥의 차이


class Comment(models.Model):

    class Meta:
        db_table="comments"

    content = models.ForeignKey('content.ContentModel', on_delete=models.CASCADE)
    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField('user.UserModel', related_name="likes", default=None, blank=True)
    like_count = models.BigIntegerField(default='0')


class LikeComment(models.Model):

    class Meta:
        db_table = "like_comments"

    comment = models.ForeignKey('content.Comment', on_delete=models.CASCADE)
    nickname = models.ForeignKey('user.UserModel', on_delete=models.CASCADE)