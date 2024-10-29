from django.contrib import admin
from .models import Product, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')  # Added stock
    search_fields = ('name',)
    list_filter = ('created_at',)

    def delete_model(self, request, obj):
        # Custom logic before deletion can go here
        super().delete_model(request, obj)  # Call the parent method to delete the object

    def delete_queryset(self, request, queryset):
        # Custom logic before deleting multiple objects can go here
        super().delete_queryset(request, queryset)  # Call the parent method to delete the queryset
