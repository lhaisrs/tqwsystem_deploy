"""teamworkquality URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from twqsystem import views

urlpatterns = [
    url(r'formulario', views.get_formulario, name='formulario'),
    url(r'relatorio', views.get_relatorio, name='relatorio'),
    url(r'relatorios', views.get_relatorios, name='relatorios'),
    #url(r'^relatorio/historico', views.get_historic_relatorio, name='historico'),
    #url(r'^relatorio/analise', views.get_analise_relatorio, name='analise'),
    #url(r'^', views.get_home, name='blog'),
]

