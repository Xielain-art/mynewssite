from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsInlines(admin.TabularInline):
    model = News
    extra = 0


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo']
    list_display_links = ['id', 'title', 'created_at', 'updated_at']
    list_editable = ['is_published']
    search_fields = ['title', 'content']
    list_filter = ['is_published', 'category']
    fields = ['title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at',
              'updated_at', ]
    readonly_fields = ['get_photo', 'views', 'created_at', 'updated_at']
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='75'>")

    get_photo.short_description = 'Миниатюра'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    inlines = [
        NewsInlines
    ]
# Register your models here.
