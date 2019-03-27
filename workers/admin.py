from django.contrib import admin
from .models import Worker


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('department', 'username',
                    'position', 'hire_date', 'salary', 'image')
    list_display_links = ('department', 'username',)
    list_filter = ('department',)
    search_fields = ('username', 'position',)


admin.site.register(Worker, WorkerAdmin)
