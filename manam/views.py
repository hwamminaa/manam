from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    3/0
    return render(request, 'manam/main.html')
