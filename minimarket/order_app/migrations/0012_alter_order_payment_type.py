# Generated by Django 4.1.7 on 2023-06-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0011_alter_order_delivery_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('1', 'Онлайн картой'), ('2', 'При получении')], default='1', max_length=30, verbose_name='Тип оплаты'),
        ),
    ]
