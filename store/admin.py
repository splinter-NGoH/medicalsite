from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name_in_inglish', 'product_name_in_arabic', 'slug', 'price', 'is_available', 'category', "created_date")
    prepopulated_fields = {'slug': ('product_name_in_inglish',)}
    search_fields = ('product_name_in_inglish', 'product_name_in_arabic', 'slug', 'price', 'is_available', 'category', "created_date")
    filter_fields = ( 'price', 'is_available', 'category', "created_date")

    
admin.site.register(Product, ProductAdmin)