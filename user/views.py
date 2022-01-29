from django.shortcuts import render

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET': #GET 메서드로 요청이 들어온 경우
        return render(request, 'user/signup.html')
    elif request.method == 'POST': #POST 메서드로 요청이 들어온 경우
        return ""
def sign_in_view(request):
    return render(request, 'user/signin.html')

