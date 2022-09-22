from django.shortcuts import render
from program.models import Program
from ku_manam.models import Question, Article
from django.db.models import Count

# Create your views here.
def index(request):
    context = {}

    question_list = Question.objects.all().annotate(likes_count=Count('like_users')).order_by('-likes_count')[0:3]
    article_list = Article.objects.all().annotate(likes_count=Count('like_users')).order_by('-likes_count')[0:3]
    program_list = Program.objects.all().annotate(likes_count=Count('like_users')).order_by('-likes_count')[0:3]
    context['program_list'] = program_list
    context['article_list'] = article_list
    context['question_list'] = question_list
    return render(request, 'manam/main.html', context)

def intro(request):
    return render(request,'manam/intro.html')

def index2(request):
    return render(request,'manam/maindraft.html')