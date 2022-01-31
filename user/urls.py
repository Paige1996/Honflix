from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'), #회원가입 URL 설정한 것
    path('sign-in/', views.sign_in_view, name='sign-in'), #로그인 URL 설정한 것
    path('logout/', views.logout, name='logout'),
]