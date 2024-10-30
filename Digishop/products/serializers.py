from rest_framework import serializers
from .models import Product, Cart, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)  # Accept product ID for input

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity', 'created_at', 'updated_at']

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')  # Extract product ID
        product_instance = Product.objects.get(id=product_id)  # Get the product instance
        cart_item = CartItem.objects.create(product=product_instance, **validated_data)
        return cart_item

    def to_representation(self, instance):
        # Customize the representation to include product details
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data  # Serialize the product
        return representation

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
