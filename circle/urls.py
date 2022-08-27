from django.urls import path

from . import views

app_name = 'circle'

urlpatterns = [
    path('', views.index, name = 'index'),
    ##광장
    path('gwangjang/', views.gwangjang, name = 'gwangjang'),
    path('gwangjang/<int:question_id>/', views.detail, name = 'detail'),
    path('gwangjang/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('gwangjang/question/create/', views.question_create, name='question_create'),
    path('gwangjang/question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('gwangjang/question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('gwangjang/answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('gwangjang/answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('gwangjang/autonomy_program/',views.autonomy_program, name='autonomy_program'), ##자율프로그램
    path('gwangjang/proposal/',views.proposal, name='proposal'),




    ##동아리 모아보기
    path('circlelist/',views.circle_list, name = 'circle_list'),
]