from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    """Функция для отображения сообщения на главной странице."""

    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    """Функция для отображения сообщения для страницы группы."""

    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'

    context = {
        'text': text
    }
    return render(request, template, context)
