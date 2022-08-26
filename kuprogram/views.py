from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Circleprogram
from .forms import QuestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Circleprogram.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(hashtag__icontains=kw) |  # 해시태그 검색
            Q(title__icontains=kw) |  # 동아리명 검색
            Q(category__icontains=kw) # 카테고리 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'kuprogram/kuprogram_main.html',context)

def detail(request, question_id):
    question = get_object_or_404(Circleprogram, pk=question_id)
    context = {'question': question}
    return render(request, 'kuprogram/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('kuprogram:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'kuprogram/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Circleprogram, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('kuprogram:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('kuprogram:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'kuprogram/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Circleprogram, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('kuprogram:detail', question_id=question.id)
    question.delete()
    return redirect('kuprogram:index')


