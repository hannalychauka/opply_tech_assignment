from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from products.models import Product
from products.serializers import ProductSerializer


class ProductAPIView(RetrieveModelMixin,
                         ListModelMixin,
                         GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Product.objects.all().order_by('name')

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
