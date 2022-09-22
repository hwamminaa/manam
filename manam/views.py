from django.shortcuts import render
from program.models import Program
from ku_manam.models import Question
from kuprogram.models import Circleprogram

# Create your views here.
def index(request):
    context = {}

    circleprogram_list = Circleprogram.objects.all()[0:3]
    question_list = Question.objects.all()[0:3]
    program_list = Program.objects.all().order_by('end_date')[:3]
    context['program_list'] = program_list
    context['circleprogram_list'] = circleprogram_list
    context['question_list'] = question_list
    return render(request, 'manam/main.html', context)

def intro(request):
    return render(request,'manam/intro.html')

def index2(request):
    return render(request,'manam/maindraft.html')