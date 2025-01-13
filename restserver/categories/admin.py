from unfold import (
    admin as unfold_admin
)

from django.contrib import admin

from .models import (
    Category,
    Subcategory
)


class SubcategoryInlines(unfold_admin.TabularInline):
    model = Subcategory


@admin.register(Category)
class CategoryAdmin(unfold_admin.ModelAdmin):
    inlines = [
        SubcategoryInlines
    ]


@admin.register(Subcategory)
class SubcategoryAdmin(unfold_admin.ModelAdmin):
    pass
