from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import pandas as pd
from .models import Facility, Category
import json
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def map(request):
    return render(request, 'facility/test.html')

def downloadFacilities(request):
    with open('C:\Korea university\데이터톤\장고\전체시설정보.json', encoding='utf-8') as json_file:
        facility = json.load(json_file)
        category_list = []

        for i in range(len(facility)):
            Facility.objects.create(
                cate_1 = facility[i]['구분'],
                name = facility[i]['시설명'],
                lat = facility[i]['lat'],
                lng = facility[i]['lng'],
                dong = facility[i]['행정동'],
                cate_2 = facility[i]['분류체계'],
                content = facility[i]['시설정보'],
                url = facility[i]['링크']
            )
            if facility[i]["구분"] not in category_list:
                Category.objects.create(name=facility[i]["구분"])
                category_list.append(facility[i]["구분"])

    return HttpResponse(f'''
        <html>
        <body>
            <h1>Download Complete</h1>
            {facility}
        </body>
        </html>
        ''')


def showFacilities(request):
    facilities = Facility.objects.all
    context = {'facilities': facilities}
    return render(request, 'facility/default.html', context)


def getlocation(request):
    location_input = request.GET.get('location_input', '')
    facilities = Facility.objects.all
    context = {'facilities': facilities, 'location_input': location_input}
    return render(request, 'facility/get_location.html', context)

def showFacilitylist(request):
        context = {}
        facility_list = Facility.objects.order_by('name')

        # 사이트에서 필터 선택 여부 받아오기
        b = request.GET.get('b', '')
        price = request.GET.get('price', '')
        print(price)

        ########## 카테고리 리스트 ###############
        category_list = Category.objects.all()
        context['category_list'] = category_list

        if b:
            facility_list = facility_list.filter(
                Q(name__icontains=b) |
                Q(cate_1__icontains=b) |
                Q(cate_2__icontains=b) |
                Q(dong__icontains=b) |
                Q(content__icontains=b)
            ).distinct()

        if price == '0':
            facility_list = facility_list
        elif price == '1':
            facility_list = facility_list.filter(cate_1= '공공도서관')
        elif price == '2':
            facility_list = facility_list.filter(cate_1= '공공체육시설')
        elif price == '3':
            facility_list = facility_list.filter(cate_1= '공연장')
        elif price == '4':
            facility_list = facility_list.filter(cate_1= '교육기관')
        elif price == '5':
            facility_list = facility_list.filter(cate_1= '도서관')
        elif price == '6':
            facility_list = facility_list.filter(cate_1= '동주민센터')
        elif price == '7':
            facility_list = facility_list.filter(cate_1= '문화시설')
        elif price == '8':
            facility_list = facility_list.filter(cate_1= '문화예술회관')
        elif price == '9':
            facility_list = facility_list.filter(cate_1= '문화원')
        elif price == '10':
            facility_list = facility_list.filter(cate_1= '미술관')
        elif price == '11':
            facility_list = facility_list.filter(cate_1= '박물관/기념관')
        elif price == '12':
            facility_list = facility_list.filter(cate_1= '아동청소년지원센터')
        elif price == '13':
            facility_list = facility_list.filter(cate_1= '작은도서관')
        elif price == '14':
            facility_list = facility_list.filter(cate_1= '노인복지시설(경로당)')
        elif price == '15':
            facility_list = facility_list.filter(cate_1= '노인여가복지시설')
        elif price == '16':
            facility_list = facility_list.filter(cate_1= '노인의료복지시설(노인요양공동생활가정)')
        elif price == '17':
            facility_list = facility_list.filter(cate_1= '노인의료복지시설(노인요양시설)')
        elif price == '18':
            facility_list = facility_list.filter(cate_1= '노인주거복지시설')
        elif price == '19':
            facility_list = facility_list.filter(cate_1= '재가노인복지시설(재가노인지원)')
        elif price == '20':
            facility_list = facility_list.filter(cate_1= '재가노인복지시설(주야간보호)')
        elif price == '21':
            facility_list = facility_list.filter(cate_1= '방과후교실')
        elif price == '22':
            facility_list = facility_list.filter(cate_1= '지역아동센터')
        elif price == '23':
            facility_list = facility_list.filter(cate_1= '틈새돌봄기관')
        elif price == '24':
            facility_list = facility_list.filter(cate_1= '거주시설')
        elif price == '25':
            facility_list = facility_list.filter(cate_1= '공동생활가정')
        elif price == '26':
            facility_list = facility_list.filter(cate_1= '단기거주시설')
        elif price == '27':
            facility_list = facility_list.filter(cate_1= '복지관1')
        elif price == '28':
            facility_list = facility_list.filter(cate_1= '복지관2')
        elif price == '29':
            facility_list = facility_list.filter(cate_1= '지역사회재활시설')
        elif price == '30':
            facility_list = facility_list.filter(cate_1= '직업재활시설')
        elif price == '31':
            facility_list = facility_list.filter(cate_1= '기타')
        elif price == '32':
            facility_list = facility_list.filter(cate_2= '교육·문화')
        elif price == '33':
            facility_list = facility_list.filter(cate_2= '노인·청소년')
        elif price == '34':
            facility_list = facility_list.filter(cate_2= '보육·가족및여성')
        elif price == '35':
            facility_list = facility_list.filter(cate_2= '사회복지일반')
        else:
            facility_list = facility_list

            # 필터 옵션
        context['b'] = b
        context['price'] = price

        # 필터링 된 결과 개수
        context['facility_number'] = facility_list.count()

        # 페이징 처리 시작
        page = request.GET.get('page', '1')  # 페이지
        paginator = Paginator(facility_list, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context['facility_list'] = page_obj

        return render(request, 'facility/facility_list.html', context)


def detail(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    context = {'facility': facility}
    return render(request, 'facility/facility_detail.html', context)
