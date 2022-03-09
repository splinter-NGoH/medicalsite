from django.shortcuts import render
from .models import Product
from category.models import Category, HomeSliedes
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def store (request, category_slug= None):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by("created_date").filter(Q(description__icontains=keyword) | Q(product_name_in_inglish__icontains=keyword) | Q(product_name_in_arabic__icontains=keyword), is_available=True)
            paginator = Paginator(products, 3) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            product_count = products.count()
        context = {
            'products': page_obj,
            'product_count': product_count,
        }
        return render(request, 'store/store.html', context)
    
    home_slides = HomeSliedes.objects.all()
    products = None
    categories = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 3) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    return render(request, 'store/store.html', {'products': page_obj, "categories":categories, "home_slides":home_slides})


def product_detail (request, category_slug, product_slug):
    product = get_object_or_404(Product,category__slug=category_slug, slug=product_slug)
    return render(request, 'store/product_detail.html', {"product": product})


def search(request):
    print("in search")
    print("in search")
    print("in search")
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by("created_date").filter(Q(description__icontains=keyword) | Q(product_name_in_inglish__icontains=keyword) | Q(product_name_in_arabic__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
