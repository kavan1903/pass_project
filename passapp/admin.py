from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'passes', 'amount', 'venue', 'created_at')
    list_filter = ('venue', 'created_at')
    search_fields = ('customer_name', 'phone', 'venue')
    readonly_fields = ('uuid', 'created_at')
    ordering = ('-created_at',)
