# Generated by Django 5.1.2 on 2024-10-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0003_alter_invoice_invoice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(blank=True, choices=[('Receipt', 'Receipt'), ('Invoice', 'Invoice')], default='Invoice', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_five_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_four_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
    ]