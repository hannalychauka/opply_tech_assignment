from django.test import TestCase, RequestFactory
from orders.views import ListOrderView
from users.models import User


class OrdersListTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='john@mail.com',
            email='john@mail.com',
            password='hello_world123!'
        )

    def test_list_view(self):
        request = self.factory.get('/api/v1/orders/')
        request.user = self.user
        response = ListOrderView.as_view()(request)
        self.assertEqual(response.status_code, 200)
