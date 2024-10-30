from django.contrib import admin
from .models import Product, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')  # Added stock
    search_fields = ('name',)
    list_filter = ('created_at',)

    def delete_model(self, request, obj):
       
        super().delete_model(request, obj)  

    def delete_queryset(self, request, queryset):
        super().delete_queryset(request, queryset)  
