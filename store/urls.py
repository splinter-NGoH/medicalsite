from django.urls import path 
from .views import store, product_detail, search



urlpatterns = [
    path('', store, name = "store"),
    path("<slug:category_by_mastercategory>/", store, name= "category_mastercategory"),
    path("<slug:category_by_mastercategory>/<slug:category_slug>/", store, name= "products_by_category"),
    path('<slug:category_by_mastercategory>/<slug:category_slug>/<slug:product_slug>', product_detail, name= "product_detail"),
    path('search/', search, name='search'),
]