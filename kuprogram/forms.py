from kuprogram.models import Circleprogram
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Circleprogram  # 사용할 모델
        fields = ['title','subject', 'category', 'content','hashtag','apply','inquiry']
        labels = {
            'title':'동아리명',
            'subject': '제목',
            'category': '카테고리',
            'content': '내용',
            'hashtag': '해시태그',
            'inquiry' : '문의 사항',
            'apply':' 신청 방법',
        }


