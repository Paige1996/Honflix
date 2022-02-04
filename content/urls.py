from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('content/<int:pk>', views.content_view, name='content'),  # 컨텐츠 추가
    path('my_page/', views.my_page_view, name='my_page'),  # 마이페이지
]
