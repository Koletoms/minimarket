# Generated by Django 4.1.7 on 2023-03-09 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0003_alter_basketproduct_count_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basketproduct',
            old_name='total_price',
            new_name='price',
        ),
    ]
