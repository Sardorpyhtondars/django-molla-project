from modeltranslation.translator import register, TranslationOptions
from blogs.models import Author, Category, Tag, Blog

@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('full_name', 'about', 'professions')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')