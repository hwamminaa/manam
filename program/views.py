from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Program
import pandas as pd
from datetime import datetime
from django.core.paginator import Paginator

import time


# Create your views here.
def downloadProgram(request):
    filename = 'C:/dataton2022/전체프로그램데이터.csv'
    df = pd.read_csv(filename, encoding="UTF-8", na_values='nan')
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
                               start_date=start_date_result, end_date=end_date_result, host=df["기관"][i])

    return HttpResponse(f'''
    <html>
    <body>
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
