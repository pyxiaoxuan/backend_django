"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR+'\\backend_django'))
import backend_django.views
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',backend_django.views.home, name='home'),
    url(r'^manifest.json$',backend_django.views.manifest),
    url(r'^asset-manifest.json$',backend_django.views.asset_manifest),
    url(r'^request/choice$',backend_django.views.getChoicePost),
    url(r'^request/blank$',backend_django.views.getCompletionPost),
    url(r'^request/calculate$',backend_django.views.getCalculationPost),
    url(r'^request/shortanswer$',backend_django.views.getEssayPost),
    url(r'^request/make$',backend_django.views.getMakePost),    
    url(r'^public/assets$',backend_django.views.getDocGet),
    url(r'^public/answer$',backend_django.views.getAnsGet),
    url(r'^paper/question1$',backend_django.views.getQ1Get),
    url(r'^paper/question2$',backend_django.views.getQ2Get),
    url(r'^paper/question3$',backend_django.views.getQ3Get),
    url(r'^paper/answer1$',backend_django.views.getA1Get),
    url(r'^paper/answer2$',backend_django.views.getA2Get),
    url(r'^paper/answer3$',backend_django.views.getA3Get),
    url(r'^time$',backend_django.views.getTimePost),
    url(r'^choice$',backend_django.views.getChoiceBody),
    url(r'^delete$',backend_django.views.getDelete),
]
