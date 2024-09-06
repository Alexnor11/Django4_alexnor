from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Войти", 'url_name': 'login'}
]

cats_db = [
    {'id': 1, 'name': 'Web develops'},
    {'id': 2, 'name': 'Games develops'},
    {'id': 3, 'name': 'Linux'},
    {'id': 4, 'name': 'Docker'},
    {'id': 5, 'name': 'Git'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,
    }
    return render(request, 'develops/index.html', context=data)


def about(request):
    return render(request, 'develops/about.html',{'title': 'О сайте', 'menu': menu})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'cat_selected': cat_id,
    }
    return render(request, 'develops/index.html', context=data)



