from django.urls import path

from . import views

app_name = 'manam'

urlpatterns = [
    path('', views.index, name='index'),
]