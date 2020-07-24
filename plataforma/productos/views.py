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

  return HttpResponse(response, content_type='text/json', status=200)


@csrf_exempt
def add_products(request):
  if request.method == 'POST':
    product_list = json.loads(request.body)

    # Validate data and return errors
    errors = validate_data(product_list["products"])
    if(len(errors) > 0):
      response = json.dumps({"status": "ERROR", "products_report" : errors})
      return  HttpResponse(response, content_type='text/json', status=422 )
    
    # Insert products
    correct_creation = insert_data(product_list["products"])
    if(correct_creation):
      response = json.dumps([{"status": "OK"}])
      return HttpResponse(response, content_type='text/json', status=200)
    
    response = json.dumps({"status": "ERROR"})
    return  HttpResponse(response, content_type='text/json', status=500 )

def insert_data(product_list):
  '''Insert the data in the BD

    Keyword arguments:
    product_list -- list of products already validate
  '''
  for product in product_list:
    new_product = Product(name=product["name"], value=product["value"], discount_value=product["discount_value"], stock=product["stock"])
    try:
      new_product.save()
    except Exception as e:
      print(e)
      return False
  return True

    
def validate_data(product_list):
  '''Validate the data before

    Keyword arguments:
    product_list -- list of products comming from the user
  '''
  error_list = []
  for product in product_list:
    errors = []
    if(len(product["name"]) < 3 or len(product["name"]) > 55 ):
      errors.append("Invalid product name")

    if(product["value"] < 0 or product["value"] > 99999.9):
      errors.append("Invalid value")
    
    if(product["discount_value"] > product["value"]):
      errors.append("Invalid discount value")
    
    if(product["stock"] < 0):
      errors.append("Invalid stock value")
    
    if(len(errors) > 0):
      error_list.append({"product_id": product["name"], "errors": errors})

  return error_list



