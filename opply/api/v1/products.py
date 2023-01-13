from django.urls import re_path

from products.views import ProductAPIView

urlpatterns = [
    re_path(r'^((?P<pk>[0-9]+)/)?$', ProductAPIView.as_view(), name='product_list')
]
