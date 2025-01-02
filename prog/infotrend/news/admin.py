from django.contrib import admin
from .models import News, Cat


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','cat', 'time_create', 'get_len_info', 'is_published')
    list_display_links = ('id', 'title')
    ordering = ['time_create']
    actions = ['set_published', 'delete_published']
    search_fields = ['title']
    list_filter = ['cat__name', 'is_published']
    prepopulated_fields = {'slug':('title', )}

    def get_len_info(self, News):
        return f"Всего: {len(News.content)} символов"

    def set_published(self, request, queryset):
        queryset.update(is_published=News.Status.PUBLISHED)

    def delete_published(self, request, queryset):
        queryset.update(is_published=News.Status.DRAFT)

admin.site.register(News, NewsAdmin)

class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links =('id', 'name')

admin.site.register(Cat, CatAdmin)