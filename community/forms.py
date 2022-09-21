from ku_manam.models import Article, Comment
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 사용할 모델
        fields = ['subject', 'category', 'content']
        labels = {
            'subject': '제목',
            'category': '종류(모집/신청)',
            'content': '내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '내용',
        }