from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'recipes/pages/index.html')


def recipe(request,id):
    return render(request, 'recipes/pages/recipe-view.html')
