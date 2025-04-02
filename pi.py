import http.client
import json
import urllib.parse
import requests
# from django.shortcuts import render, get_object_or_404
# from .store import search

# conn = http.client.HTTPSConnection("real-time-amazon-data.p.rapidapi.com")

# headers = {
#                 'x-rapidapi-key': "7debb7ebcamsh697fec96085fa39p1af17djsn93536afedd97",
#                 'x-rapidapi-host': "real-time-amazon-data.p.rapidapi.com"
# }
# search_query = input("Enter the product name: ")
# encoded_query = urllib.parse.quote(search_query)
# conn.request("GET", f'/search?query={encoded_query}&page=1&country=US&sort_by=RELEVANCE&product_condition=ALL&is_prime=false&deals_and_discounts=NONE', headers=headers)

# res = conn.getresponse()
# data = res.read()
# print(data)
# ds= json.loads(data.decode("utf-8"))
# pretty_data = json.dumps(ds, indent=4)
# print(pretty_data)
# products = ds['data']['products']
# for product in products:
#     p_name = product['product_title']
#     p_price = product['product_price']
#     p_img = product['product_photo']
#     p_url = product['product_url']
#     p_desc =  product.get('description', 'No description available')
#     print(p_name)
#     print(p_price)
#     print(p_img)
#     print(p_url)
#     print(p_desc)
# p_desc =  products[0].get('description', 'No description available')
# for p_name in p_name:
#     print(p_name)   
# print(p_price)
# print(p_img)
# print(p_url)
# print(p_desc)


# print(ds)
# import http.client

# conn = http.client.HTTPSConnection("real-time-product-search.p.rapidapi.com")

# headers = {
#     'x-rapidapi-key': "7314a7cb81msh911d0e5a0909807p1f9e5cjsn86b3d95ccd07",
#     'x-rapidapi-host': "real-time-product-search.p.rapidapi.com"
# }
# search_query = input("Enter the product name: ")
# # encoded_query = urllib.parse.quote(search_query)
# # conn.request("GET", "/search?q={encoded_query}&country=IN&language=en&page=1&limit=10&sort_by=BEST_MATCH&product_condition=ANY&min_rating=ANY", headers=headers)

# # res = conn.getresponse()
# # data = res.read()
# # ds= json.loads(data.decode("utf-8"))
# # pretty_data = json.dumps(ds, indent=4)
# # print(pretty_data)
# # print(data.decode("utf-8"))

import http.client
search_query = input("Enter the product name: ")

conn = http.client.HTTPSConnection("google-search-master.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7314a7cb81msh911d0e5a0909807p1f9e5cjsn86b3d95ccd07",
    'x-rapidapi-host': "google-search-master.p.rapidapi.com"
}

encoded_query = urllib.parse.quote(search_query)

conn.request("GET", f"/shopping?q={encoded_query}&gl=in&hl=en&autocorrect=true&num=10&page=1", headers=headers)
res = conn.getresponse()
data = res.read()
ds= json.loads(data.decode("utf-8"))
pretty_data = json.dumps(ds, indent=4)
print(pretty_data)
print(data)