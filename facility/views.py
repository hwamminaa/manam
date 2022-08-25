from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import pandas as pd
from .models import Facility
import json
from django.core.paginator import Paginator

# Create your views here.
def map(request):
    return render(request, 'facility/test.html')

def downloadFacilities(request):
    with open('C:\Korea university\데이터톤\장고\전체시설정보.json', encoding='utf-8') as json_file:
        facility = json.load(json_file)

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
    page = request.GET.get('page', '1')  # 페이지
    program_list = Facility.objects.order_by('name')
    paginator = Paginator(program_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'facility_list': page_obj}
    return render(request, 'facility/facility_list.html', context) # 객체 있으면 세번째 parameter: context

def detail(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    context = {'facility': facility}
    return render(request, 'facility/facility_detail.html', context)


