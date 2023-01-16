from django.test import TestCase, RequestFactory
from products.models import Product
from products.views import ProductAPIView
from users.models import User


class CreateProductCase(TestCase):
    def setUp(self):
        Product.objects.create(name='phone', price=10, quantity_in_stock=50)

    def test_object_attributes(self):
        product = Product.objects.get(name='phone')
        self.assertEqual(product.price, 10)
        self.assertEqual(product.quantity_in_stock, 50)


class ProductsListTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='john@mail.com',
            email='john@mail.com',
            password='hello_world123!'
        )

    def test_list_view(self):
        request = self.factory.get('/api/v1/products/')
        request.user = self.user
        response = ProductAPIView.as_view()(request)
        self.assertEqual(response.status_code, 200)
