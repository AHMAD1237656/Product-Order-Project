from django.contrib import admin
from .models import Product, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'email', 'phone', 'address', 'message', 'created_at')

    def has_add_permission(self, request):
        return False  # ❌ Disable manual add

    def has_change_permission(self, request, obj=None):
        return False  # ❌ Disable manual edit

admin.site.register(Order, OrderAdmin)
admin.site.register(Product)  # Product ko allow rehne dein
