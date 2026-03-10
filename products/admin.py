from django.contrib import admin
from products.models import Category, Product, ProductImage, Review
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title', 'parent', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title', 'category', 'price', 'old_price', 'stock', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['category', 'is_featured', 'created_at']
    inlines = [ProductImageInline]