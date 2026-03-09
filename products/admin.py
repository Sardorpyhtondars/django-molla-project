from django.contrib import admin
from products.models import Category, Product, ProductImage, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price', 'old_price', 'stock', 'is_featured', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'author_name', 'rating', 'created_at']
    search_fields = ['author_name', 'email', 'comment']
    list_filter = ['rating', 'created_at']