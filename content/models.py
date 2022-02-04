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
    video_simlilar = models.URLField(max_length=2000)
    thumbnailURL = models.URLField(max_length=2000)
    videoURL = models.URLField(max_length=2000)
    categories = models.ForeignKey('content.Category', related_name="categories", on_delete=models.CASCADE)
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


class LikeComment(models.Model):

    class Meta:
        db_table = "like_comments"

    comment = models.ForeignKey('content.Comment', on_delete=models.CASCADE)
    nickname = models.ForeignKey('user.UserModel', on_delete=models.CASCADE)


