from django.shortcuts import render, HttpResponse
import pandas as pd
from .models import Facility
import json

# Create your views here.
def map(request):
    return render(request, 'facility/test.html')

def showFacilities(request):
    with open('C:\dataton2022\전체시설정보.json', encoding='utf-8') as json_file:
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

    facilities = Facility.objects.all
    return render(request, 'facility/default.html', {'facilities': facilities})

def getlocation(request, location_input):
    with open('C:\dataton2022\전체시설정보.json', encoding='utf-8') as json_file:
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
    location_input = request.GET.get('location_input', '')
    facilities = Facility.objects.all
    return render(request, 'facility/get_location.html', {'facilities': facilities, 'location_input': location_input})

