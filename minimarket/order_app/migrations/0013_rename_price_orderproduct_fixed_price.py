# Generated by Django 4.1.7 on 2023-06-07 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0012_alter_order_payment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='price',
            new_name='fixed_price',
        ),
    ]
