from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone', 'email', 'passes', 'amount', 'venue', 'created_at']
    list_filter = ['created_at', 'venue']
    search_fields = ['customer_name', 'phone', 'email']
    ordering = ['-created_at']
