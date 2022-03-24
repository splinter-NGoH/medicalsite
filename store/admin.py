from django.contrib import admin
from .models import Product, CustomerRequests, HomeReviews, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name_in_inglish', 'product_name_in_arabic', 'slug', 'price', 'is_available',  "created_date")
    prepopulated_fields = {'slug': ('product_name_in_inglish',)}
    search_fields = ('product_name_in_inglish', 'product_name_in_arabic', 'slug', 'price', 'is_available',  "created_date")
    filter_fields = ( 'price', 'is_available', 'category', "created_date")

    
admin.site.register(Product, ProductAdmin)


class CustomerRequestsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'note', 'created_at')
    search_fields = ('full_name', 'phone_number', 'email', 'note', 'created_at')
    filter_fields = ( 'full_name', 'phone_number', 'phone_number', "created_at")

    
admin.site.register(CustomerRequests, CustomerRequestsAdmin)


class HomeReviewsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'description')
    search_fields = ('full_name', 'department', 'description')
    filter_fields = ('full_name', 'department', 'description')

    
admin.site.register(HomeReviews, HomeReviewsAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'images', 'created_date', 'modified_date')
    filter_fields = ('created_date', 'modified_date')

    
admin.site.register(ProductImage, ProductImageAdmin)