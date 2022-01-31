from django.shortcuts import render, redirect
from .models import ContentModel
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    user = request.user.is_authenticated
    #HOEM이라는 함수를 실행시키는 것 만으로도 사용자가 로그인 되어있는지 안되있는지 알 수있음
    if user: #이 사용자가 있으면
        return redirect('/main')
    else:
        return redirect('/sign-in')


def main(request): #get 방식만
    if request.method =='GET':
        user = request.user.is_authenticated
        if user:
            all_content = ContentModel.objects.all()
            return render(request, 'main/main.html', {'contents':all_content})
        else:
            return redirect('/sign-in')
