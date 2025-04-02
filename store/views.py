from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import category
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import http.client
import requests
import json
import urllib.parse
# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:   
        categories = get_object_or_404(category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html',context)


import requests
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def product_detail(request, category_slug, product_slug):
   
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
      
   
   
    context = {
        'single_product': single_product,
       
    }
    return render(request, 'store/product_detail.html', context)
# def product_detail(request, product_name, asin):
#     # Ensure you're using the parameters correctly
#     try:
#         local_product = get_object_or_404(Product, slug=product_name, asin=asin)

#         # Mock API connection or additional logic
#         product_title = local_product.product_name
#         product_price = local_product.price
#         product_description = local_product.description

#         context = {
#             'product_title': product_title,
#             'product_price': product_price,
#      

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword','').strip()

        if keyword:
            local_products = Product.objects.order_by('-created').filter(Q(description__icontains=keyword )| Q(product_name__icontains=keyword) )
            product_count = local_products.count()

        conn = http.client.HTTPSConnection("google-search-master.p.rapidapi.com")
        # 'x-rapidapi-key': "7debb7ebcamsh697fec96085fa39p1af17djsn93536afedd97",
        headers = {
           'x-rapidapi-key': "7314a7cb81msh911d0e5a0909807p1f9e5cjsn86b3d95ccd07",
           'x-rapidapi-host': "google-search-master.p.rapidapi.com"
        }
        
        encoded_query = urllib.parse.quote(keyword)

        conn.request("GET", f"/shopping?q={encoded_query}&gl=in&hl=en&autocorrect=true&num=10&page=1", headers=headers)
        res = conn.getresponse()
        data = res.read()
       

        ds = json.loads(data.decode("utf-8"))
        if 'shopping' in ds and isinstance(ds['shopping'], list):
            products = ds['shopping']  # List of products from API
        else:
            products = []  # Default to an empty list if no products are found

        # Simulate local products (replace with a query from your database)
        local_products = [
            {"title": "Local Product 1", "price": "₹1,500.00", "source": "Local Store"},
            {"title": "Local Product 2", "price": "₹1,800.00", "source": "Local Vendor"}
        ]

        # Prepare context
        context = {
            'local_products': local_products,  # Local products from your database
            'products': products,              # API products as a list
        }

    return render(request, "store/search_result.html", context)



