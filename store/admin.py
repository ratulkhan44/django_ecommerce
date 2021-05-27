from django.contrib import admin
from .models import Product, Tax

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category',
                    'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Tax)
