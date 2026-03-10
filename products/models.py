from django.db import models
from shared.models import BaseModel

class Category(BaseModel):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )
    stock = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def discount_percent(self):
        if self.old_price and self.old_price > self.price:
            return int((self.old_price - self.price) / self.old_price * 100)
        return 0

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Image for {self.product.title}"

    class Meta:
        db_table = 'product_image'
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Review(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='reviews'
    )
    author_name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.author_name} — {self.product.title}"

    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'