# Generated by Django 5.0.6 on 2025-07-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passapp', '0008_invoice_paid_amount_alter_invoice_payment_mode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Partially Paid', 'Partially Paid')], default='Unpaid', max_length=20),
        ),
    ]
