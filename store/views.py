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



# # !pip install requests

# # !pip install beautifulsoup4
# from bs4 import BeautifulSoup
# import requests
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
# flipkart=''
# amazon=''
# def flipkart(name):
#     try:
#         global flipkart
#         name1 = name.replace(" ","+")
#         flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
#         res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)


#         print("\nSearching in flipkart....")
#         soup = BeautifulSoup(res.text,'html.parser')
        
#         if(soup.select('._4rR01T')):
#             flipkart_name = soup.select('._4rR01T')[0].getText().strip().upper()
#             if name.upper() in flipkart_name:
#                 flipkart_price = soup.select('._30jeq3')[0].getText().strip()
#                 flipkart_name = soup.select('._4rR01T')[0].getText().strip()
#                 print("Flipkart:")
#                 print(flipkart_name)
#                 print(flipkart_price)
#                 print("---------------------------------")
                
#         elif(soup.select('.s1Q9rs')):
#             flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
#             flipkart_name = flipkart_name.upper()
#             if name.upper() in flipkart_name:
#                 flipkart_price = soup.select('._30jeq3')[0].getText().strip()
#                 flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
#                 print("Flipkart:")
#                 print(flipkart_name)
#                 print(flipkart_price)
#                 print("---------------------------------")
#         else:
#             flipkart_price='0'
            
#         return flipkart_price 
#     except:
#         print("Flipkart: No product found!")  
#         print("---------------------------------")
#         flipkart_price= '0'
#     return flipkart_price

# def amazon(name):
#     try:
#         global amazon
#         name1 = name.replace(" ","-")
#         name2 = name.replace(" ","+")
#         amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
#         res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
#         print("\nSearching in amazon...")
#         soup = BeautifulSoup(res.text,'html.parser')
#         amazon_page = soup.select('.a-color-base.a-text-normal')
#         amazon_page_length = int(len(amazon_page))
#         for i in range(0,amazon_page_length):
#             name = name.upper()
#             amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
#             if name in amazon_name:
#                 amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip()
#                 amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
#                 amazon_description = soup.select('.a-text-normal')[i].getText().strip()
#                 amazon_image = soup.select('.s-image')[i]['src']
#                 print("Amazon:")
#                 print(amazon_name)
#                 print("₹"+amazon_price)
#                 print("---------------------------------")
#                 break
#             else:
#                 i+=1
#                 i=int(i)
#                 if i==amazon_page_length:
#                     amazon_price = '0'
#                     print("amazon : No product found!")
#                     print("-----------------------------")
#                     break
                    
#         return amazon_price
#     except:
#         print("Amazon: No product found!")
#         print("---------------------------------")
#         amazon_price = '0'
#     return amazon_price

# def convert(a):
#     b=a.replace(" ",'')
#     c=b.replace("INR",'')
#     d=c.replace(",",'')
#     f=d.replace("₹",'')
#     g=int(float(f))
#     return g

# name=input("Product Name:\n")
# flipkart_price=flipkart(name)
# amazon_price=amazon(name)


# if flipkart_price=='0':
#     print("Flipkart: No product found!")
#     flipkart_price = int(flipkart_price)
# else:
#     print("\nFlipkart Price:",flipkart_price)
#     flipkart_price=convert(flipkart_price)
# if amazon_price=='0':
#     print("Amazon: No product found!")
#     amazon_price = int(amazon_price)
# else:
#     print("\nAmazon price: ₹",amazon_price)
#     amazon_price=convert(amazon_price)