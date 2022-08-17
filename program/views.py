from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Program, Category
import pandas as pd
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q

import time


# Create your views here.
def downloadProgram(request):
    filename = 'C:/dataton2022/현재진행중인프로그램.csv'
    df = pd.read_csv(filename, encoding="UTF-8", na_values='nan')
    category_list = []
    for i in range(len(df)):
        # 기간 format 변경 (str > date)
        start_date_string = df["기간시작"][i]
        start_date_format = "%Y.%m.%d"
        start_date_result = datetime.strptime(start_date_string, start_date_format)
        end_date_string = df["기간끝"][i]
        end_date_format = "%Y.%m.%d"
        end_date_result = datetime.strptime(end_date_string, end_date_format)
        # 프로그램 데이터 db에 저장
        Program.objects.create(name=df["프로그램명"][i], type=df["유형"][i],
                               category=df["카테고리"][i], age=df["연령대"][i], price=df["비용"][i],
                               start_date=start_date_result, end_date=end_date_result) # , host=df["기관"][i])
        if df["카테고리"][i] not in category_list:
            Category.objects.create(name=df["카테고리"][i])
            category_list.append(df["카테고리"][i])
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


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    program_list = Program.objects.order_by('-start_date')
    paginator = Paginator(program_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'program_list': page_obj}
    return render(request, 'program/program_list.html', context) # 객체 있으면 세번째 parameter: context


def detail(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    context = {'program': program}
    return render(request, 'program/program_detail.html', context)


def answer_create(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    context = {'program': program}
    return render(request, 'program/program_result.html', context)


def index2(request):
    page = request.GET.get('page', '1')  # 페이지
    program_list = Program.objects.order_by('-start_date')
    paginator = Paginator(program_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'program_list': page_obj}
    return render(request, 'program/program_search.html', context) # 객체 있으면 세번째 parameter: context


def program_search(request):
    # program_list = Program.objects.all()

    paginate_by = 15
    context = {}

    b = request.GET.get('b', '')
    f = request.GET.getlist('f')
    price = request.GET.get('price', '')
    program_list = Program.objects.order_by('-start_date')
    print(price)

    ########## 장르 리스트 ###############
    category_list = Category.objects.all()
    context['category_list'] = category_list

    if b or f or price:
        if b:
            program_list = program_list.filter(
                Q(name__icontains=b) |
                Q(category__icontains=b)
            ).distinct()

        if f:
            print(f)
            query = Q()
            for i in f:
                query = query | Q(category__icontains=i)
                program_list = program_list.filter(query)

        if price == '0':
            program_list = program_list.filter(price=0)
        elif price == '1':
            program_list = program_list.filter(price=20000)
        elif price == '2':
            program_list = program_list.filter(price=30000)
        elif price == '3':
            program_list = program_list.filter(price=40000)
        elif price == '4':
            program_list = program_list.filter(price=50000)
        else:
            program_list = program_list.filter(price=50000)

    context['is_paginated'] = True
    paginator = Paginator(program_list, paginate_by)
    page_number_range = 15  # 페이지그룹에 속한 페이지 수
    # CBV에서 self.request: HttpRequest
    # request.POST : POST 방식으로 넘어온 요청파라미터 조회
    # request.GET : GET 방식으로 넘어온 요청파라미터 조회
    current_page = int(request.GET.get('page', 1))
    context['current_page'] = current_page
    # 시작/끝 index 조회
    start_index = int((current_page - 1) / page_number_range) * page_number_range
    end_index = start_index + page_number_range

    # 현재 페이지가 속한 페이지 그룹의 범위
    current_page_group_range = paginator.page_range[start_index: end_index]
    print("current_page_group_range", current_page_group_range)

    start_page = paginator.page(current_page_group_range[0])
    end_page = paginator.page(current_page_group_range[-1])

    has_previous_page = start_page.has_previous()
    has_next_page = end_page.has_next()

    context['current_page_group_range'] = current_page_group_range
    if has_previous_page:  # 이전페이지 그룹이 있다면
        context['has_previous_page'] = has_previous_page
        context['previous_page'] = start_page.previous_page_number

    e = paginate_by * current_page
    s = e - paginate_by
    print("내용 index", s, e)

    program_list = program_list[s:e]

    context['program_list'] = program_list


    #return HttpResponse(f'''{category_list}''')

    return render(request, 'program/program_search.html', context)


