from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import AddPostForm, UploadFileForm
from .models import Alexnor, Category, UploadFiles

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'develops/index.html', context=data)


class AlexBlog(ListView):
    queryset = Alexnor.published.all().select_related('cat')
    template_name = 'develops/blog.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,
    }

    # def get_queryset(self):
    #     return Alexnor.published.all().select_related('cat')


# class AlexBlog(TemplateView):
#     template_name = 'develops/blog.html'
#     extra_context = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'posts': Alexnor.published.all(),
#         'cat_selected': 0,
#     }


# def blog(request):
#     posts = Alexnor.published.all()
#     data = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'posts': posts,
#     }
#
#     return render(request, 'develops/blog.html', context=data)


def about(request):
    return render(request, 'develops/about.html',
                  {'title': 'О сайте', 'menu': menu})


# def show_post(request, post_slug):
#     post = get_object_or_404(Alexnor, slug=post_slug)
#
#     data = {
#         'title': post.title,
#         'menu': menu,
#         'post': post,
#         'cat_selected': 1,
#     }
#     return render(request, 'develops/post.html', context=data)


class ShowPost(DetailView):
    model = Alexnor
    template_name = 'develops/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Alexnor.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(View):
    pass


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


class AlexCategory(ListView):
    template_name = 'develops/blog.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория - ' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.id
        return context

    def get_queryset(self):
        return Alexnor.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Alexnor.published.filter(cat_id=category.pk)
#     data = {
#         'title': f'Рубрика: {category.name}',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': category.pk,
#     }
#     return render(request, 'develops/blog.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
