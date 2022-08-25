from django.urls import path

from . import views

app_name = 'program'

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.downloadProgram, name='download'),
    path('<int:program_id>/', views.detail, name='detail'),
    path('<int:program_id>/result', views.answer_create, name='result'),
    path('search/', views.program_search, name='search'),
    path('downloadRecommendation/', views.downloadRecommendation, name='downloadRecommendation'),
]