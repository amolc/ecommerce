from unfold import (
    admin as unfold_admin
)

from django.contrib import admin

from .models import (
    Organisation
)


@admin.register(Organisation)
class OrganisationAdmin(unfold_admin.ModelAdmin):
    pass
