from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Alexnor, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(Alexnor)
class DevelopsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'is_published']
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat', 'post_photo')
    readonly_fields = ['post_photo']
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 20
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True

    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, develops: Alexnor):
        if develops.photo:
            return mark_safe(f"<img src='{develops.photo.url}' width=50>")
        return "Без фото"

    @admin.action(description="Опубликовать выбранные Материалы")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Alexnor.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Снять с публикации выбранные Материалы")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Alexnor.Status.DRAFT)
        self.message_user(request, f"{count} записи(ей) сняты с публикации!",
                          messages.WARNING)
