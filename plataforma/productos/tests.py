from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    def test_create_product(self):
        product = Product(name="Plumon", value=10.5, discount_value=5, stock=5 )
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(str(product), '%s %s %s %s' % (product.name, product.value, product.discount_value, product.stock))

class ProductAPITest(TestCase):

    def test_list_product(self):
        '''
        Test to verify that a get call return a 200 status
        '''
        response = self.client.get("/api/products")     
        self.assertEqual(200, response.status_code)

    def test_can_add_product(self):
        '''
        Test to verify that a post add a product whith valid values
        '''
        data = {
            "products":[
                {
                    "name": "Dulces",
                    "value": 50,
                    "discount_value": 10,
                    "stock": 2
                }
            ]
        }
        response = self.client.post("/api/products/bulk_insert", data=data, content_type="application/json")
        self.assertEqual(200, response.status_code)

    def test_error_add_product(self):
        '''
        Test to verify that a post return an erro when the data is wrong
        '''
        data = {
            "products":[
                {
                    "name": "Dulces",
                    "value": 1,
                    "discount_value": 10,
                    "stock": 2
                }
            ]
        }
        response = self.client.post("/api/products/bulk_insert", data=data, content_type="application/json")
        self.assertEqual(422, response.status_code)
