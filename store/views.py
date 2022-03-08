from django.shortcuts import render
from .models import Product
from category.models import Category
from django.shortcuts import get_object_or_404

def store (request, category_slug= None):
    if category_slug is None:
        products = Product.objects.all().filter(is_available= True).order_by('created_date')
        categories = Category.objects.all()
    else:
        categories = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=categories)

    return render(request, 'store/store.html', {'products': products, "categories":categories})


def product_detail (request, category_slug, product_slug):
    product = get_object_or_404(Product,category__slug=category_slug, slug=product_slug)
    return render(request, 'store/product_detail.html', {"product": product})