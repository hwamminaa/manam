import json
import sys,io,os
import django
from .models import Facility

def showFacilities(request):
    with open('C:\Korea university\데이터톤\장고\전체시설정보.json', encoding='utf-8') as json_file:
        facility = json.load(json_file)

    facilitydict = []
    for i in range(len(facility)):
        facilitydict.append({
            "구분": facility[i]['구분'],
            "시설명": facility[i]['시설명'],
            "lat": facility[i]['lat'],
            "lng": facility[i]['lng'],
            "행정동": facility[i]['행정동'],
            "분류체계": facility[i]['분류체계'],
            "시설정보": facility[i]['시설정보'],
            "링크": facility[i]['링크'],
        })
    return facilitydict


if __name__ == '__main__':
    facility = showFacilities()

    for i in range(len(facility)):
        Facility(
            cate_1 = facilitiy[i]['구분'],
            name = facility[i]['시설명'],
            lat = facility[i]['lat'],
            lng = facility[i]['lng'],
            dong = facility[i]['행정동'],
            cate_2 = facility[i]['분류체계'],
            content = facility[i]['시설정보'],
            url = facility[i]['링크']
        ).save()
