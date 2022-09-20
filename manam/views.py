from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'manam/main.html')

def intro(request):
    return render(request,'manam/intro.html')

def index2(request):
    return render(request,'manam/main2.html')