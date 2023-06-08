# Generated by Django 4.1.7 on 2023-03-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0008_alter_basketproduct_fixed_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketproduct',
            name='count',
        ),
        migrations.AddField(
            model_name='basketproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=2, verbose_name='Quantity'),
            preserve_default=False,
        ),
    ]
