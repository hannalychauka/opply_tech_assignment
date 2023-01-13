from django.urls import path

from orders.views import ListOrderView, CreateOrderView

urlpatterns = [
    path('', ListOrderView.as_view(), name='orders_list'),
    path('create/', CreateOrderView.as_view(), name='order_create'),
]
