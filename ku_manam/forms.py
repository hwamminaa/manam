from ku_manam.models import Question, Answer
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['title','subject', 'category', 'content','hashtag','inquiry','apply']
        labels = {
            'title': '동아리명',
            'subject': '제목',
            'category': '카테고리',
            'content': '내용',
            'hashtag': '해시태그',
            'inquiry': '문의 사항',
            'apply': '신청 방법'
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '내용',
        }