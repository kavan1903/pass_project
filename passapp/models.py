import uuid
from django.db import models

# passapp/models.py

class Invoice(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('Cash', 'Cash'),
        ('Online', 'Online'),
        ('Split', 'Split'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Partially Paid', 'Partially Paid'),
        
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(default="")
    passes = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # 🆕
    venue = models.CharField(max_length=200, default="")
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES, default='Cash')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')  # 🆕
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.paid_amount >= self.amount:
            self.payment_status = 'Paid'
        elif self.paid_amount > 0:
            self.payment_status = 'Partially Paid'
        else:
            self.payment_status = 'Unpaid'
        super().save(*args, **kwargs)
