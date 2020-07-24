from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productos.models import Product
from django.core import serializers



def list_products(request):
  if request.method == 'GET':
    try:
      products = serializers.serialize('json',Product.objects.all())
      response = products
    except:
      response = json.dumps([{'Error': "Can't get the product list"}])

  return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_products(request):
  if request.method == 'POST':
    product_list = json.loads(request.body)
    for product in product_list["products"]:
      print(product["name"])
      new_product = Product(name=product["name"], value=product["value"], discount_value=product["discount_value"], stock=product["stock"])
      try:
        new_product.save()
      except Exception as e:
        print(e)

    response = json.dumps([{'Success': 'Car created'}])
  return HttpResponse(response, content_type='text/json')


