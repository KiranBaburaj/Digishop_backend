from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CartItem, Cart
from .serializers import CartItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        # Allow admin users to perform create, update, and delete operations
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = []  # Allow any authenticated user to view products
        return super().get_permissions()

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only retrieve the cart for the authenticated user
        return self.queryset.filter(user=self.request.user)

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter cart items for the authenticated user's cart
        return self.queryset.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the cart based on the authenticated user
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

    def update(self, request, *args, **kwargs):
        # Update item quantity
        cart_item = self.get_object()
        quantity = request.data.get("quantity")
        if quantity:
            cart_item.quantity = quantity
            cart_item.save()
        return Response(CartItemSerializer(cart_item).data)

    def destroy(self, request, *args, **kwargs):
        # Delete the cart item
        cart_item = self.get_object()
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
