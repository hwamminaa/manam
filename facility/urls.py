
from django.urls import path
from facility import views

app_name = "facility"

urlpatterns = [
    path('download/', views.downloadFacilities, name='download'),
    path('facilitylist/', views.showFacilities, name='facilitylist'),
    path('facilitylist/getlocation/', views.getlocation, name='location_input'),
    path('showFacilitylist', views.showFacilitylist, name='showFacilitylist'),
    path('showFacilitylist/<int:facility_id>/', views.detail, name='detail'),
]
