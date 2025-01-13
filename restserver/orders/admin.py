from unfold import (
    admin as unfold_admin
)

from django.contrib import admin

from. models import (
    Order,
    OrderItem,
    OrderStatusChange,
    OrderPaymentStatusChange,    
)


class OrderItemInline(unfold_admin.TabularInline):
    model = OrderItem


class OrderStatusChangeInline(unfold_admin.TabularInline):
    model = OrderStatusChange


class OrderPaymentStatusChangeInline(unfold_admin.TabularInline):
    model = OrderPaymentStatusChange


@admin.register(Order)
class OrderAdmin(unfold_admin.ModelAdmin):
    inlines = [
        OrderItemInline,
        OrderStatusChangeInline,
        OrderPaymentStatusChangeInline,        
    ]
