from django.urls import path
from . import views

app_name = 'community'

urlpatterns=[
    path('', views.allarticles, name = 'allarticles'),
    path('recruitment/', views.recruitment, name='recruitment'),
    path('proposal/',views.proposal, name = 'proposal'),

    path('allarticles/<int:article_id>/', views.detail, name='detail'),
    path('allarticles/answer/create/<int:article_id>/', views.answer_create, name='answer_create'),
    path('allarticles/question/create/', views.question_create, name='question_create'),
    path('allarticles/question/modify/<int:article_id>/', views.question_modify, name='question_modify'),
    path('allarticles/question/delete/<int:article_id>/', views.question_delete, name='question_delete'),
    path('allarticles/answer/modify/<int:comment_id>/', views.answer_modify, name='answer_modify'),
    path('allarticles/answer/delete/<int:comment_id>/', views.answer_delete, name='answer_delete'),
    path('allarticles/<int:article_id>/like', views.like, name='like'),
]