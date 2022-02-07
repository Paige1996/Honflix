from django.shortcuts import render, redirect
from content.models import ContentModel, Comment
from user.models import WishList
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import ast
import requests
import json



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


@login_required()
def content_view(request, pk):  # = urls.py
    content = ContentModel.objects.get(pk=pk)

    similar_list = []
    for similar in content.get_video_similar():
        similar_content = ContentModel.objects.filter(videoURL=f'https://www.youtube.com/embed/{similar}')
        similar_list.extend(list(similar_content))
    content.video_similar = similar_list
    print(similar_list)
    all_comment = Comment.objects.filter(content=content).order_by('-created_at') #여기 중요
    return render(request, 'main/content.html',{"content":content, "comments": all_comment} ) # "comments"딕셔와 content.html에 for문 일치


@login_required()
def write_comment(request, pk):
    if request.method == 'POST':
        comment = request.POST.get('comment_box', '')
        current_content = ContentModel.objects.get(pk=pk)

        ContentCommnet = Comment()
        ContentCommnet.user = request.user
        ContentCommnet.description = comment
        ContentCommnet.content = current_content
        ContentCommnet.save()

        return redirect('/content/' + str(pk))

@login_required()
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    current_content = comment.content.id
    comment.delete()
    return redirect('/content/' + str(current_content))



