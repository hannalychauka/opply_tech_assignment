from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from orders.models import Order, OrderProductMapping
from products.models import Product
from products.serializers import ProductSerializer


class OrderedProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProductMapping
        fields = ('product', 'amount')


class ListOrderSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ('status', 'delivery_address', 'ordered_products', 'created_at')


class OrderedProductCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    amount = serializers.IntegerField()


class CreateOrderSerializer(serializers.Serializer):
    ordered_products = OrderedProductCreateSerializer(many=True)
    delivery_address = serializers.CharField()

    def validate(self, attrs):
        for product_data in attrs.get('ordered_products', []):
            if not Product.objects.filter(id=product_data.get('id')).exists():
                raise ValidationError(
                    {'detail': 'Some products do not exist'}
                )
            left_amount = Product.objects.get(id=product_data.get('id')).quantity_in_stock
            if product_data.get('amount') > left_amount:
                raise ValidationError(
                    {'detail': f'You cannot order more than {left_amount}.'}
                )
        return attrs
