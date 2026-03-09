from django.contrib import admin
from blogs.models import Author, Category, Tag, Blog


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'professions', 'is_active', 'created_at']
    search_fields = ['full_name', 'professions']
    list_filter = ['is_active', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_at']
    search_fields = ['title', 'short_description', 'long_description']
    list_filter = ['status', 'authors', 'categories', 'tags', 'created_at']