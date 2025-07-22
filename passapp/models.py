import uuid
from django.db import models

# passapp/models.py

class Invoice(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(default=True)  # ✅ Add this field
    passes = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    venue = models.CharField(max_length=200, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
