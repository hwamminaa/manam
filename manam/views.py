from django.shortcuts import HttpResponse, render

import logging
logger = logging.getLogger('manam')

# Create your views here.
def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'manam/main.html')
