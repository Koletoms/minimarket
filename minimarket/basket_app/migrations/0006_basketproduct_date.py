# Generated by Django 4.1.7 on 2023-03-09 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0005_rename_price_basketproduct_fixed_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketproduct',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
