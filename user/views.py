from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserModel, WishList
from content.models import ContentModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 있는지 검수하는 함수
from django.contrib import auth # 사용자 auth 가능


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET': #GET 메서드로 요청이 들어온 경우
        user = request.user.is_authenticated # 로그인 된 사용자가 요청하는지 검사
        if user: # 로그인이 되어있다면
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST': #POST 메서드로 요청이 들어온 경우
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        nickname = request.POST.get('nickname', '')
        email = request.POST.get('email', '')

        if username == '' :
            return render(request, 'user/signup.html', {'error': '아이디를 적어주세요'})
        elif password == '':
            return render(request, 'user/signup.html', {'error': '비밀번호를 적어주세요'})
        elif nickname == '':
            return render(request, 'user/signup.html', {'error': '닉네임을 적어주세요'})
        elif email == '':
            return render(request, 'user/signup.html', {'error': '이메일을 적어주세요'})
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error': '아이디가 이미 존재합니다'})
            else:
                UserModel.objects.create_user(username=username, password=password, nickname=nickname, email=email)
                return redirect('/sign-in') #회원가입이 완료되었으므로 로그인 페이지로 이동

def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated #사용자가 로그인 되어 있는지 검사
        if user: #로그인이 되어 있다면
            return redirect('/')
        else:
            return render(request, 'user/signin.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password) #암호화된 비밀번호와 현재 입력된 비밀번호가 일치하는지, 그게 사용자와 맞는지까지 한번에 확인
        if me is not None: #사용자가 있다
            auth.login(request, me) #장고가 알아서 로그인도 관리, 나의 정보를 넣어줌
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': '아이디 혹은 패스워드를 확인 해 주세요'})

@login_required
def logout(request):
    auth.logout(request) #인증되어있는 정보를 없애기
    return redirect("/")


@login_required()
def my_page_view(request, pk):
    user = UserModel.objects.get(pk=pk)

    all_wish = user.wishList.all()
    return render(request, 'main/my_page.html', {'user':user, 'wishlists': all_wish})


@login_required()
def my_page_bookmark(request, pk):
    if request.method == 'POST':
        content = ContentModel.objects.get(pk=pk)
        if request.user.wishList.filter(pk=content.pk).exists():
            request.user.wishList.remove(content)
        else:
            request.user.wishList.add(content)

        return redirect('/content/' + str(pk))





#기존 것
@login_required()
def save_wish2(request):
    user = request.user.is_authenticated
    if user: #로그인 유저가 있다면
        if request.method == 'GET':
            return redirect('/content')
        elif request.method == 'POST':
            content = request.POST.get('content','')
            wishlists = WishList.objects.all()
            if content not in wishlists: #위시리스트에 콘텐트가 없다면
                WishList.objects.create(content=content)#위시리스트에 담아준다.
            else:
                WishList.objects.remove()