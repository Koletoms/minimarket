# Generated by Django 4.1.7 on 2023-03-25 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0008_delivery_available_alter_delivery_above_price_limit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Delivery', 'verbose_name_plural': 'Deliveries'},
        ),
    ]
