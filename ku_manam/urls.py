from django.urls import path

from . import views

app_name = 'ku_manam'

urlpatterns = [
    path('', views.index, name = 'index'),
    ##동아리 재능기부
    path('talent_donation/', views.talent_donation, name = 'talent_donation'),

    ##동아리 모아보기
    path('circlelist/',views.circle_list, name = 'circle_list'),


    path('circlelist/<int:question_id>/', views.detail, name = 'detail'),
    path('talent_donation/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('talent_donation/question/create/', views.question_create, name='question_create'),
    path('talent_donation/question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('talent_donation/question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('talent_donation/answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('talent_donation/answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('talent_donation/<int:question_id>/likes/',views.likes, name='likes'),
    path('talent_donation/<int:question_id>/like/',views.like, name='like'),
    path('talent_donation/optimal/', views.optimal, name='optimal'),

]