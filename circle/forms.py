from circle.models import Question, Answer
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'category', 'content']
        labels = {
            'subject': '제목',
            'category': '종류(모집/신청)',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '내용',
        }