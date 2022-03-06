from django.contrib import admin

from .models import Product, ProductCost, ProductCount, Customer, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


class ProductCountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'begin',
        'end',
        'value',
    )


class ProductCostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'begin',
        'end',
        'value',
    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'orders_count'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'date_formation',
        'customer'
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'product',
        'count'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCount, ProductCountAdmin)
admin.site.register(ProductCost, ProductCostAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
