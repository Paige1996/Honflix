from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('content/<int:pk>', views.content_view, name='content'),  # 컨텐츠 추가
    path('content/comment/<int:pk>', views.write_comment, name='write-comment'),
    path('content/comment/delete/<int:pk>', views.delete_comment, name='delete-comment'),
    path('like/<int:comment_pk>/<int:content_pk>', views.like, name='like'),
]