from django.urls import path, register_converter
from . import views
from . import converters
# from .views import AlexBlog, AlexCategory, ShowPost

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.AlexIndex.as_view(), name='home'),
    path('blog/', views.AlexBlog.as_view(), name='blog'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.AlexCategory.as_view(), name='category'),
]
