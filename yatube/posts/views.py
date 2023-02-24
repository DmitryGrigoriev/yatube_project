from django.shortcuts import render

# Create your views here.


def index(request):
    """Функция для отображения сообщения на главной странице."""

    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'

    context = {
        'text': text
    }

    return render(request, template, context)


def group_post(request, slug):
    """Функция для отображения сообщения для страницы группы."""

    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'

    context = {
        'text': text
    }
    return render(request, template, context)
