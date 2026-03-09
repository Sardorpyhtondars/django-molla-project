from django.db import models
from shared.models import BaseModel


class Author(BaseModel):
    full_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='authors/', default='authors/default-user.jpg')
    about = models.CharField(max_length=255)
    professions = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Category(BaseModel):
    title = models.CharField(max_length=128)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class BlogStatus(models.TextChoices):
    PUBLISHED = "PUBLISHED", "Published"
    DRAFT = "DRAFT", "Draft"
    DELETED = "DELETED", "Deleted"


class Blog(BaseModel):
    title = models.CharField(max_length=128)
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs/', default='blogs/default-blog.jpg')
    long_description = models.TextField()
    status = models.CharField(
        max_length=24,
        choices=BlogStatus.choices,
        default=BlogStatus.DRAFT
    )
    categories = models.ManyToManyField(Category, related_name='blogs')
    tags = models.ManyToManyField(Tag, related_name='blogs')
    authors = models.ManyToManyField(Author, related_name='blogs')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'