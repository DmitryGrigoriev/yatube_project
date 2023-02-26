from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Create your views here.


def index(request):
    """Функция для выведения 10 последних записей."""

    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    """Функция для отображения сообщения для страницы группы."""

    group = get_object_or_404(Group, slug=slug)
    posts = Post.object.filter(group=group).order_by('-pub_date')[:10]

    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
