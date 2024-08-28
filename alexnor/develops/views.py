from django.http import HttpResponse

from django.template.loader import render_to_string
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'develops/index.html')


def about(request):
    return render(request, 'develops/about.html')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        return redirect('cats','python', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p> {year}</p>")
