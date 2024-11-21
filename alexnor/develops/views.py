from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from .forms import AddPostForm, UploadFileForm
from .models import Alexnor, Category, UploadFiles
from .utils import DataMixin


class AlexIndex(DataMixin, ListView):
    queryset = Alexnor.published.all().select_related('cat')
    template_name = 'develops/index.html'
    context_object_name = 'posts'


class AlexBlog(DataMixin, ListView):
    queryset = Alexnor.published.all().select_related('cat')
    template_name = 'develops/blog.html'
    context_object_name = 'posts'


def about(request):
    return render(request, 'develops/about.html',
                  {'title': 'О сайте',})


def contact(request):
    data = {
        # 'menu': menu,
        'title': 'Форма обратной связи'
    }
    return render(request, 'develops/contact.html', context=data)


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DataMixin, DetailView):
    model = Alexnor
    template_name = 'develops/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Alexnor.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'develops/addpage.html'
    title_page = 'Добавление статьи'


class AlexCategory(DataMixin, ListView):
    template_name = 'develops/blog.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.pk,
                                      )

    def get_queryset(self):
        return Alexnor.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
