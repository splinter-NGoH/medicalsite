from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from store.models import Product, HomeReviews
from category.models import HomeSliedes
from store.forms import CustomerRequestsForm
from django.contrib import messages

def home (request):
    home_slides = HomeSliedes.objects.all()
    home_reviews = HomeReviews.objects.all()
    products = Product.objects.all().filter(is_available= True).order_by('created_date')[:5]

    if request.method == 'POST':
        form = CustomerRequestsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('وصلنا طلبك هنتواصل معاكك في اقرب وقت'))
            return redirect('home')
    else:
        form = CustomerRequestsForm()

    return render(request, 'home.html', {"products":products, "home_slides":home_slides,"home_reviews":home_reviews, "form": form})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')