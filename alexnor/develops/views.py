from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddPostForm, UploadFileForm
from .models import Alexnor, Category, UploadFiles

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Alexnor.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }

    return render(request, 'develops/index.html', context=data)


def about(request):
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         fp = UploadFiles(file=form.cleaned_data['file'])
    #         fp.save()
    # else:
    #     form = UploadFileForm()
    return render(request, 'develops/about.html',
                  {'title': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Alexnor, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'develops/post.html', context=data)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'develops/addpage.html', context=data)


def contact(request):
    data = {
        'menu': menu,
        'title': 'Форма обратной связи'
    }
    return render(request, 'develops/contact.html', context=data)


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Alexnor.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'develops/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
