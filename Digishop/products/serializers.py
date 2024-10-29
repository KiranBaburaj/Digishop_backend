from rest_framework import serializers
from .models import Product, Cart, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'created_at', 'updated_at']

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, source='cartitem_set')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items', 'created_at', 'updated_at', 'total_price']

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cartitem_set', [])
        cart = Cart.objects.create(**validated_data)
        for item_data in cart_items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart
