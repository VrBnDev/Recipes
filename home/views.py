from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def recipe(request,id):
    return render(request, 'index.html')
