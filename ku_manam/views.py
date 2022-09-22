from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseNotAllowed


def index(request):
    return render(request, 'ku_manam/index.html')

def circle_list(request):
    return render(request, 'circlelist/circle_search.html')

def talent_donation(request):

    context = {}
    b = request.GET.get('b', '')  # 검색어
    f = request.GET.getlist('f')
    
    question_list = Question.objects.order_by('-create_date')
    if b:
        question_list = question_list.filter(
            Q(subject__icontains=b) |  # 제목 검색
            Q(content__icontains=b) |  # 내용 검색
            Q(category__icontains=b) |
            Q(title__icontains=b) |
            Q(hashtag__icontains=b)
        ).distinct()
    if f:
        print(f)
        query = Q()
        for i in f:
            query = query | Q(category__icontains=i)
        question_list = question_list.filter(query)

    context['question_number'] = question_list.count()
    page = request.GET.get('page','1')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context['question_list'] = page_obj
    return render(request, 'ku_manam/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'ku_manam/question_detail.html', context)

def likes(request, question_id):
    if request.user.is_authenticated:
        article = get_object_or_404(Question, pk=question_id)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('ku_manam:talent_donation')
    return redirect('common:login')

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('ku_manam:talent_donation')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'ku_manam/question_form.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('ku_manam:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'ku_manam/question_detail.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('ku_manam:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('ku_manam:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'ku_manam/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('ku_manam:talent_donation')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('ku_manam:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('ku_manam:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'ku_manam/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        answer.delete()
    return redirect('ku_manam:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def like(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user in question.like_users.all():
        question.like_users.remove(question.author)
    else:
        question.like_users.add(request.user)
    return redirect('ku_manam:detail', question.id)

def optimal(request):
    return render(request, 'ku_manam/optimal.html')

def optimal2(request):
    return render(request, 'ku_manam/optimal2.html')

def yangji(request):
    return render(request, 'ku_manam/yangji.html')

def kusep(request):
    return render(request, 'ku_manam/kusep.html')

def alleyopt(request):
    return render(request, 'ku_manam/alleyopt.html')

def observer(request):
    return render(request, 'ku_manam/observer.html')