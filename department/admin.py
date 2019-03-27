from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_display_links = ('name',)


admin.site.register(Department, DepartmentAdmin)
