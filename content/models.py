from django.db import models
from user.models import UserModel

# Create your models here.

class ContentModel(models.Model):
    class Meta:
        db_table = "content"

    title = models.CharField(max_length=100)
    description = models.TextField()
    postImageURL = models.URLField(max_length=2000)
    thumbnailURL = models.URLField(max_length=2000)
    videoURL = models.URLField(max_length=2000)

    categories = models.ManyToManyField("Category", through="ContentCategory", related_name="categories")
    # related_name :어떻게 찾기를 원하는가. 카테고리를 찾을때 이름.
    comments = models.ManyToManyField(UserModel, through="Comment", related_name="comments")
    wishLists = models.ManyToManyField(UserModel, through="WishList", related_name="wishlists")

    # "Class_name" = 클래스 이름. Q ""와 그냥의 차이

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table="categories"

class ContentCategory(models.Model):
    content = models.ForeignKey(ContentModel, on_delete=models.CASCADE) # cascade 컨텐츠가 삭제되면 컨텐츠 카테고리도 자동으로 삭제된다.
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # 카테고리가 삭제되면 컨텐츠카테고리도 자동으로 삭제된다.
    class Meta:
        db_table="content_categories"

class Comment(models.Model):
    content = models.ForeignKey(ContentModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="comments"

class LikeComment(models.Model):
    comment= models.ForeignKey(Comment, on_delete=models.CASCADE)
    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    class Meta:
        db_table="like_comments"

class WishList(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.ForeignKey(ContentModel, on_delete=models.CASCADE)
    class Meta:
        db_table= "wishlists"