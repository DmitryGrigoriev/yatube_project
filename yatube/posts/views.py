from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Функция для отображения сообщения на главной странице."""

    template = 'posts/index.html'
    return render(request, template)


def group_post(request, slug):
    """Функция для отображения сообщения для страницы группы."""

    return HttpResponse(f'Ты на странице {slug}')
