from django import forms
from .models import Invoice

# passapp/forms.py

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'phone', 'email', 'passes', 'amount', 'venue']  # ✅ Add email
