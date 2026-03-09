from django.shortcuts import render, get_object_or_404
from blogs.models import Blog, BlogStatus, Category, Tag


def blogs_list_view(request):
    context = {
        'blogs': Blog.objects.filter(status=BlogStatus.PUBLISHED),
        'categories': Category.objects.filter(parent=None).prefetch_related('children'),
        'tags': Tag.objects.all(),
        'recent_posts': Blog.objects.filter(status=BlogStatus.PUBLISHED).order_by('-created_at')[:3],
    }
    return render(request, 'blogs/blog.html', context)


def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk, status=BlogStatus.PUBLISHED)
    context = {
        'blog': blog,
        'recent_posts': Blog.objects.filter(status=BlogStatus.PUBLISHED).exclude(pk=pk).order_by('-created_at')[:3],
        'tags': Tag.objects.all(),
        'categories': Category.objects.filter(parent=None),
    }
    return render(request, 'blogs/single.html', context)