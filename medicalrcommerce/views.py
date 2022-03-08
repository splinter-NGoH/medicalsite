from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.utils.translation import gettext_lazy as _
from store.models import Product
def home (request):
    products = Product.objects.all().filter(is_available= True).order_by('created_date')[:5]
    return render(request, 'home.html', {"products":products})