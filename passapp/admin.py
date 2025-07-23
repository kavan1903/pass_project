from django.contrib import admin
from .models import Invoice

# passapp/admin.py

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name', 'phone', 'email',
        'passes', 'amount', 'paid_amount',
        'venue', 'payment_mode', 'payment_status',
        'created_at', 'uuid',
    )
    list_filter = ('payment_mode', 'payment_status', 'created_at')
    search_fields = ('customer_name', 'phone', 'email', 'venue', 'uuid')
    readonly_fields = ('uuid', 'created_at')

