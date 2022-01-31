from multiprocessing import context
from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponse
from .import views
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory


def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html')


def about(request):
    return render(request,'about.html')
    #return HttpResponse('about')

def about(request):
    form = UserCreationForm()
    context = {'form' : form}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    return render(request,'signup.html',context)
    #return HttpResponse('login')    

