from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Привет, ты на главной странице")


def group_post(request, slug):
    return HttpResponse(f"Ты на странице {slug}")
