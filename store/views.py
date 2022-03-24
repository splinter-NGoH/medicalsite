from django.shortcuts import render
from .models import Product, ProductImage
from category.models import Category, HomeSliedes, MasterCategory
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def store (request, category_slug= None, category_by_mastercategory=None):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by("created_date").filter(Q(description__icontains=keyword) | Q(product_name_in_inglish__icontains=keyword) | Q(product_name_in_arabic__icontains=keyword), is_available=True)
            paginator = Paginator(products, 20) # Show 25 contacts per page.
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
    if category_by_mastercategory != None:
        if category_slug != None:
            mastercategory = get_object_or_404(MasterCategory, slug=category_by_mastercategory)
            categories = get_object_or_404(Category, slug=category_slug, master_category=mastercategory)
            products = Product.objects.filter(category=categories, is_available=True)
            paginator = Paginator(products, 25) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        else:
            mastercategory = get_object_or_404(MasterCategory, slug=category_by_mastercategory)
            categories = Category.objects.filter(master_category=mastercategory)
            products = Product.objects.filter(category__id__in=categories , is_available=True).order_by('-created_date')
            paginator = Paginator(products, 25) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    else:
        mastercategory = MasterCategory.objects.all()
        categories = Category.objects.all()
        products = Product.objects.all()
        paginator = Paginator(products, 25) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request, 'store/store.html', {'products': page_obj, "categories":categories, "home_slides":home_slides, "mastercategory":mastercategory})


def product_detail (request, category_slug, product_slug, category_by_mastercategory):
    product = get_object_or_404(Product,category__slug=category_slug, slug=product_slug)
    product_image = ProductImage.objects.filter(product=product)
    return render(request, 'store/product_detail.html', {"product": product, "product_image":product_image})


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
