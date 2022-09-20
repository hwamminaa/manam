from django.urls import path

from . import views

app_name = 'manam'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('intro/', views.intro, name='intro'),
    path('main/', views.index2, name='index2'),
]