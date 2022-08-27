from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Circleprogram, Category
from .forms import QuestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index(request):
    return render(request, 'kuprogram/kuprogram_main.html')

def search(request):
    context = {}
    b = request.GET.get('b', '')  # 검색어
    f = request.GET.getlist('f')
    question_list = Circleprogram.objects.order_by('-create_date')

    ########## 카테고리 리스트 ###############
    category_list = Category.objects.all()
    context['category_list'] = category_list

    if b:
        question_list = question_list.filter(
            Q(title__icontains=b) |  # 동아리명 검색
            Q(subject__icontains=b) |  # 제목 검색
            Q(content__icontains=b) |  # 내용 검색
            Q(hashtag__icontains=b) | # 해시태그 검색
            Q(category__icontains=b)
        ).distinct()

    if f:
        print(f)
        query = Q()
        for i in f:
            query = query | Q(category__icontains=i)
        question_list = question_list.filter(query)

    context['program_number'] = question_list.count()

    # 페이징 처리 시작
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context['question_list'] = page_obj

    return render(request, 'kuprogram/kuprogram_search.html',context)

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
            return redirect('kuprogram:search')
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
    return redirect('kuprogram:search')


