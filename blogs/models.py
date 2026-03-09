from django.db import models
from shared.models import BaseModel


class Author(BaseModel):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='authors/', null=True, blank=True)
    about = models.TextField(blank=True)
    professions = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Category(BaseModel):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Blog(BaseModel):
    class Status(models.TextChoices):
        PUBLISHED = 'published', 'Published'
        DRAFT = 'draft', 'Draft'

    title = models.CharField(max_length=300)
    short_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    long_description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    authors = models.ManyToManyField(Author, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'