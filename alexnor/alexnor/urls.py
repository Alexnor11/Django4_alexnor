from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from alexnor import settings
from develops.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('develops.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found


admin.site.site_header = "Панель управления"
admin.site.index_title = "Сайт alexnor.ru"
