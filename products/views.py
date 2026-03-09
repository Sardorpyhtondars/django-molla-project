from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product, Category, Review


def product_list_view(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(parent=None).prefetch_related('children')

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    query = request.GET.get('q')
    if query:
        products = products.filter(title__icontains=query)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
        'query': query,
    }
    return render(request, 'products/category.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=pk)[:4]

    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        email = request.POST.get('email')
        rating = request.POST.get('rating', 5)
        comment = request.POST.get('comment')

        if author_name and email and comment:
            Review.objects.create(
                product=product,
                author_name=author_name,
                email=email,
                rating=rating,
                comment=comment
            )
            messages.success(request, 'Your review has been submitted!')
            return redirect('products:detail', pk=pk)
        else:
            messages.error(request, 'Please fill in all required fields.')

    context = {
        'product': product,
        'related_products': related_products,
        'reviews': product.reviews.all(),
        'images': product.images.all(),
    }
    return render(request, 'products/product.html', context)


@login_required
def cart_view(request):
    return render(request, 'cart/cart.html')


@login_required
def checkout_view(request):
    return render(request, 'cart/checkout.html')


@login_required
def wishlist_view(request):
    return render(request, 'cart/wishlist.html')