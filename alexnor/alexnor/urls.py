from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('develops.urls')),

]

admin.site.site_header = "Панель управления"
admin.site.index_title = "Сайт Alexnor.ru"
