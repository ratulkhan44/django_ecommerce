from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, unique=True)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='images/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('store:product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class Tax(models.Model):
    tax_name = models.CharField(max_length=100, blank=True)
    rate = models.FloatField()
    is_active = models.BooleanField(default=False)
    tax_session = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tax_session
