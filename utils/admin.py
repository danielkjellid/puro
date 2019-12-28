from django.contrib import admin

from .models import ChangeLog


class ChangeLogAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'content_type', 
        'object_id', 
        'content_object', 
        'changes',
        'date_of_change'
    ]

admin.site.register(ChangeLog, ChangeLogAdmin)
