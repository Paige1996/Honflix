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

# @login_required()
# def save_wish(request):
#     user = request.user.is_authenticated
#     if user:
#         if request.method == 'GET':
#             return render(request, 'main/content.html')
#         elif request.method == 'POST':
#             content = request.POST.get('content','')
#             wishlists = WishList.objects.all()
#             if content not in wishlists:
#                 wishlists.add(content)
#             else:
#                 wishlists.remove(content)
#             return redirect('/content')

# @login_required()
# def save_wish2(request):
#     user = request.user.is_authenticated
#     if user: #로그인 유저가 있다면
#         if request.method == 'GET':
#             return redirect('/content')
#         elif request.method == 'POST':
#             content = request.POST.get('content','') #html에서 post로 받은, 즉 현재 보여지고 있는 컨텐츠
#             concon = ContentModel.objects.all() #ContentModel object 전체를 받아와서 concon에 저장
#             contentURL = concon.videoURL # concon의 videoURL을 contentURL이란 변수에 저장
#             wishlists = WishList.objects.all() #wishlists는 wishlist의 object전체를 가져오는것
#             for URL in contentURL: #contentURL이란 변수에 저장되어 있는 Content의 videourl을 for문으로 돌림
#                 if URL == content: #만약 현재 보고있는 페이지의 videourl과 ContentModel안의 값이 같다면
#                     if content not in wishlists: #위시리스트에 콘텐트가 없다면
#                         WishList.objects.create(content=content)#위시리스트에 담아준다.
#                     else:
#                         WishList.objects.remove()
#                 else: #만약 현재 보고있는 페이지의 videoURL과 ContentModel안의 값과 다르다면
#                     continue

# @login_required()
# def save_wish2(request):
#     user = request.user.is_authenticated
#     if user: #로그인 유저가 있다면
#         if request.method == 'GET':
#             return redirect('/content')
#         elif request.method == 'POST':
#             content = request.POST.get('content','') #html에서 post로 받은, 즉 현재 보여지고 있는 컨텐츠
#             wishlists = WishList.objects.all() #wishlists는 wishlist의 object전체를 가져오는것
#             if content not in wishlists: #위시리스트에 콘텐트가 없다면
#                 WishList.objects.create(user=user, content=content)#위시리스트에 담아준다.
#             else:
#                 WishList.objects.remove()

