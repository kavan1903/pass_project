import uuid
from django.db import models

class Invoice(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    passes = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    venue = models.CharField(max_length=200,default=True)  # ✅ New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.amount}"
