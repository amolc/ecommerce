# from unfold import (
#     admin as unfold_admin,
# )

from django.contrib import admin

from .models import (
    Staff,
    StaffLog
)


# class StaffLogInline(unfold_admin.TabularInline):
#     model = StaffLog


# @admin.register
# class StaffAdmin(unfold_admin.ModelAdmin):
#     model = Staff
