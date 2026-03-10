from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from blogs.models import Author, Category, Tag, Blog

@admin.register(Author)
class AuthorAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'full_name', 'is_active', 'created_at']
    search_fields = ['full_name', 'professions']
    list_filter = ['is_active', 'created_at']

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']

@admin.register(Tag)
class TagAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']

@admin.register(Blog)
class BlogAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title', 'status', 'created_at']
    search_fields = ['title', 'short_description', 'long_description']
    list_filter = ['status', 'authors', 'categories', 'tags', 'created_at']