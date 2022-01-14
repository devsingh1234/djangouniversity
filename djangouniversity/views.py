from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponse
from .import views
from django.shortcuts import render


def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html')


def about(request):
    return render(request,'about.html')
    #return HttpResponse('about')

def about(request):
    return render(request,'login.html')
    #return HttpResponse('login')    