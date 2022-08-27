from django.urls import path

from . import views

app_name = 'kuprogram'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('showprogram/', views.search, name='search'),
    path('showprogram/<int:question_id>/', views.detail, name = 'detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
]