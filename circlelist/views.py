from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import pandas as pd
from .models import Circle, Category
from django.core.paginator import Paginator
from django.db.models import Q


def downloadCircle(request):
    filename = 'C:\Korea university\데이터톤\장고\동아리전체데이터.csv'
    df = pd.read_csv(filename, encoding="cp949", na_values='nan')

    category_list = []
    for i in range(len(df)):
        # 프로그램 데이터 db에 저장
        Circle.objects.create(name=df["동아리명"][i],
                              category=df["분과"][i],
                              tag=df["해시태그"][i],
                              content=df["동아리설명"][i],
                              type=df["소속"][i])
        if df["분과"][i] not in category_list:
            Category.objects.create(name=df["분과"][i])
            category_list.append(df["분과"][i])
    return HttpResponse(f'''
    <html>
    <body>
        <h1>카테고리 이름</h1>
        <h1>Download Complete</h1>
        {df}
        <h2>Data Types</h2>
        {df.dtypes}
    </body>
    </html>
    ''')


def detail(request, circle_id):
    circle = get_object_or_404(Circle, pk=circle_id)
    context = {'circle': circle}
    return render(request, 'circlelist/circle_detail.html', context)

def circle_search(request):

    context = {}

    #사이트에서 필터 선택 여부 받아오기
    b = request.GET.get('b', '')
    f = request.GET.getlist('f')
    circle_list = Circle.objects.order_by('name')

    ########## 카테고리 리스트 ###############
    category_list = Category.objects.all()
    context['category_list'] = category_list

    if b:
        circle_list = circle_list.filter(
            Q(name__icontains=b) |
            Q(category__icontains=b) |
            Q(tag__icontains=b) |
            Q(content__icontains=b) |
            Q(type__icontains=b)
        ).distinct()

    if f:
        print(f)
        query = Q()
        for i in f:
            query = query | Q(category__icontains=i)
        circle_list = circle_list.filter(query)


    # 필터링 된 결과 개수
    context['circle_number'] = circle_list.count()

    # 페이징 처리 시작
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(circle_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context['circle_list'] = page_obj

    return render(request, 'circlelist/circle_search.html', context)