"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from manam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manam/', include('manam.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('facility/', include('facility.urls')),
    path('program/', include('program.urls')),
    path('ku_manam/',include('ku_manam.urls')),
    path('ku_manam/circlelist/', include('circlelist.urls')),
    path('community/', include('community.urls')),
]

handler404 = 'common.views.page_not_found'
