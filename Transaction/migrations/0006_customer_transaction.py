# Generated by Django 4.0.5 on 2022-07-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction', '0005_remove_customer_last_transection'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='transaction',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
