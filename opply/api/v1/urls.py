from django.urls import path, include

from api.v1 import auth, products, orders

app_name = 'v1'

urlpatterns = [
    path('auth/', include(auth.urlpatterns)),
    path('orders/', include(orders.urlpatterns)),
    path('products/', include(products.urlpatterns)),
]
