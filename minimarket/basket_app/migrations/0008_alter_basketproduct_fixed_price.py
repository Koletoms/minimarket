# Generated by Django 4.1.7 on 2023-03-11 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0007_alter_basketproduct_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketproduct',
            name='fixed_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Total price'),
        ),
    ]
