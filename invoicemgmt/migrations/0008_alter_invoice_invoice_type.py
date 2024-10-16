# Generated by Django 5.1.2 on 2024-10-16 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0007_alter_invoice_invoice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(blank=True, choices=[('Receipt', 'Receipt'), ('Invoice', 'Invoice')], default='Invoice', max_length=50, null=True),
        ),
    ]