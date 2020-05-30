# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Reading

# Register your models here.
class ReadingAdmin(admin.ModelAdmin):
    search_fields = ['nmi','meter_serial_number']
    list_display = ['nmi', 'meter_serial_number', 'meter_reading_value', 'reading_date_time', 'file_name']

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Search by NMI or Meter Serial Number'}
        return super(ReadingAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


admin.site.register(Reading, ReadingAdmin)
