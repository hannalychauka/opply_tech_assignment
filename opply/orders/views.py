from django.db import transaction
from django.db.models import Prefetch, F
from django.http import HttpResponse
from rest_framework import status as rest_status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from orders.models import Order, OrderProductMapping
from orders.serializers import ListOrderSerializer, CreateOrderSerializer
from products.models import Product


class ListOrderView(ListAPIView):
    serializer_class = ListOrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', )

    def get_queryset(self):
        return Order.objects.filter(
            customer=self.request.user
        ).prefetch_related(
            Prefetch(
                'ordered_products',
            )
        ).order_by('created_at')


class CreateOrderView(CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        products = validated_data.pop('ordered_products', [])
        with transaction.atomic():
            order = Order.objects.create(
                customer=self.request.user,
                **validated_data
            )
            ordered_products_list = []
            for product_data in products:
                ordered_products_list.append(
                    OrderProductMapping(
                        order=order,
                        **product_data
                    )
                )
                Product.objects.filter(id=product_data['id']).annotate(
                    new_quantity=F('quantity_in_stock') - product_data['amount']
                ).update(
                    quantity_in_stock=F('new_quantity')
                )
            OrderProductMapping.objects.bulk_create(ordered_products_list)
        return HttpResponse(status=rest_status.HTTP_201_CREATED)
