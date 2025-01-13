from unfold import (
    admin as unfold_admin
)

from django.contrib import admin

from .models import (
    Product,
)


@admin.register(Product)
class ProductAdmin(unfold_admin.ModelAdmin):
    pass
