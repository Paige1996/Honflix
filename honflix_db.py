import os
import django
import csv
import sys

# 프로젝트 이름.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "honflix.settings")
django.setup()

from content.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음

# csv파일 경로
CSV_PATH_PRODUCTS = 'honflix.csv'
with open(CSV_PATH_PRODUCTS, encoding='UTF8') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)  # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
    for row in data_reader:
        content = ContentModel()
        cate = Category.objects.get(name=row[0])
        content.categories = cate
        content.videoURL = f'https://www.youtube.com/embed/{row[1]}'
        content.title = row[2]
        content.keywords = row[3]
        content.thumbnailURL = row[4]
        content.description = row[5]

        content.save()

        print(row[0],row[1],row[2],row[3],row[4],row[5])

# json화 된 파일 불러오기
# def view_movie_data():
#     hi = MovieModel.objects.get(code=171539)
#     print(hi.get_actor())
#     print(hi.get_genre())
# view_movie_data()
