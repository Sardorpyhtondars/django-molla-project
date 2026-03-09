from django.contrib import messages
from django.shortcuts import render, redirect

from blogs.models import Blog, BlogStatus
from products.models import Product, Category as ProductCategory
from shared.forms import ContactForm


def home_page_view(request):
    context = {
        'featured_products': Product.objects.filter(is_featured=True)[:8],
        'categories': ProductCategory.objects.filter(parent=None)[:6],
        'recent_blogs': Blog.objects.filter(status=BlogStatus.PUBLISHED).order_by('-created_at')[:3],
    }
    return render(request, 'shared/home.html', context)


def about_us_view(request):
    return render(request, 'shared/about.html')


def contact_view(request):
    if request.method == 'GET':
        return render(request, 'shared/contact.html')
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f'{field}: {error}')
            messages.error(request, ' | '.join(errors))
        return render(request, 'shared/contact.html')


def page_404_view(request, exception=None):
    return render(request, 'shared/404.html', status=404)