from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 있는지 검수하는 함수
from django.contrib import auth # 사용자 auth 가능

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET': #GET 메서드로 요청이 들어온 경우
        return render(request, 'user/signup.html')
    elif request.method == 'POST': #POST 메서드로 요청이 들어온 경우
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        nickname = request.POST.get('nickname', None)
        email = request.POST.get('email', None)

        if username is None or password is None or nickname is None or email is None:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html') #사용자가 존재하기 때문에, 사용자를 저장하지 않고 회원가입 페이지 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password, nickname=nickname, email=email)
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'GET':
        return render(request, 'user/signin.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password) #암호화된 비밀번호와 현재 입력된 비밀번호가 일치하는지, 그게 사용자와 맞는지까지 한번에 확인
        if me is not None: #사용자가 있다
            auth.login(request, me) #장고가 알아서 로그인도 관리, 나의 정보를 넣어줌
            return HttpResponse("로그인 성공!")
        else:
            return redirect('/sign-in')


#signup.html에 추가해야할 것들
#회원가입 form 태그 찾아서 거기에
# <form class="form-area" method="post" action="/sign-up/">
# {% csrf_token %}
# <input>태그 체크하기

#유창님 signup.html에서 e-mail 되어있는거 email이랑 맞추기

#signin.html에 추가해야할 것들
#로그인 form 태그 추가해주기
# <form class="form=area" method="post" action="/sign-in/">
# {% crsf_token %}
# <input>태그 체크하기