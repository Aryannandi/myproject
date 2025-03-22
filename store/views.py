from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import category
from django.http import HttpResponse
from django.db.models import Q
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


def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created').filter(Q(description__icontains=keyword )| Q(product_name__icontains=keyword) )
            product_count = products.count()
    context = {
                'products': products,
                'product_count': product_count,
            }


    return render(request, 'store/store.html',context)