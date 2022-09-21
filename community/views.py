from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ku_manam.models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseNotAllowed

def allarticles(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    article_list = Article.objects.order_by('-create_date')
    if kw:
        article_list = article_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw)   # 내용 검색
        ).distinct()
    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'community/allarticles.html', context)

##자율동아리 모집
def recruitment(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = "모집"
    article_list = Article.objects.order_by('-create_date')
    if kw:
        article_list = article_list.filter(
            Q(category="모집")
        ).distinct()
    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj}
    return render(request, 'community/recruitment.html', context)

##프로그램 신청
def proposal(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = "신청"
    article_list = Article.objects.order_by('-create_date')
    if kw:
        article_list = article_list.filter(
            Q(category="신청")
        ).distinct()
    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj}
    return render(request, 'community/proposal.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'community/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.create_date = timezone.now()
            article.save()
            return redirect('community:allarticles')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'community/question_form.html', context)

@login_required(login_url='common:login')
def answer_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.article = article
            comment.save()
            return redirect('community:detail', article_id=article.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'article': article, 'form': form}
    return render(request, 'community/question_detail.html', context)

@login_required(login_url='common:login')
def question_modify(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('community:detail', article_id=article.id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.modify_date = timezone.now()  # 수정일시 저장
            article.save()
            return redirect('community:detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'community/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('community:detail', article_id=article.id)
    article.delete()
    return redirect('community:allarticles')

@login_required(login_url='common:login')
def answer_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('community:detail', article_id=comment.article.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('community:detail', article_id=comment.article.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'community/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        comment.delete()
    return redirect('community:detail', article_id=comment.article.id)