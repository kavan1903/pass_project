# passapp/forms.py

from django import forms
from .models import Invoice
import re

class InvoiceForm(forms.ModelForm):
    payment_mode = forms.ChoiceField(
        choices=Invoice.PAYMENT_MODE_CHOICES,
        widget=forms.RadioSelect
    )
    payment_status = forms.ChoiceField(
        choices=Invoice.PAYMENT_STATUS_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Invoice
        fields = [
            'customer_name', 'phone', 'email',
            'passes', 'amount', 'paid_amount', 'venue',
            'payment_mode', 'payment_status'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'passes': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.fullmatch(r'\d{10}', phone):
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone

    def clean_passes(self):
        passes = self.cleaned_data.get('passes')
        if passes < 1:
            raise forms.ValidationError("Number of passes must be at least 1.")
        return passes

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Total amount must be greater than 0.")
        return amount

    def clean_paid_amount(self):
        paid = self.cleaned_data.get('paid_amount')
        if paid < 0:
            raise forms.ValidationError("Paid amount cannot be negative.")
        return paid

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        paid = cleaned_data.get('paid_amount')

        if amount is not None and paid is not None and paid > amount:
            self.add_error('paid_amount', "Paid amount cannot exceed total amount.")
