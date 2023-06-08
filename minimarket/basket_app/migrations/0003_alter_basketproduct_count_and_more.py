# Generated by Django 4.1.7 on 2023-03-09 11:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('basket_app', '0002_remove_basketproduct_basket_basketproduct_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketproduct',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='session_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='session_keys', to='sessions.session'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='total_price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Total price'),
        ),
    ]