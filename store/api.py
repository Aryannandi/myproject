import http.client
import json
import urllib.parse
import requests
from django.shortcuts import render, get_object_or_404
from . import views
def amazon_products(request,search):
    
    conn = http.client.HTTPSConnection("real-time-amazon-data.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "7314a7cb81msh911d0e5a0909807p1f9e5cjsn86b3d95ccd07",
        'x-rapidapi-host': "real-time-amazon-data.p.rapidapi.com"
    }
    # search_query = keyword
    encoded_query = urllib.parse.quote(search)

    conn.request("GET", f'/search?query={encoded_query}&page=1&country=IN&sort_by=RELEVANCE&product_condition=ALL&is_prime=false&deals_and_discounts=NONE', headers=headers)

    res = conn.getresponse()
    data = res.read()
    # print(data)
    ds= json.loads(data.decode("utf-8"))

    # pretty_data = json.dumps(ds, indent=4)
    # print(pretty_data)
    products = ds['data']['products']
    for product in products:
        # p_name = product['product_title']
        # p_price = product['product_price']
        # p_img = product['product_photo']
        p_url = product['product_url']
        # p_desc =  product.get('description', 'No description available')
        # print(p_name)
        # print(p_price)
        # print(p_img)
        print(p_url)
        # print(p_desc)
    

    context = {
        # 'product_name': p_name,
        # 'product_price': p_price,
        # 'product_image': p_img,
        'product_url': p_url,
        # 'product_desc': p_desc,
    }

    return render(request, "store/search_result.html", context)
