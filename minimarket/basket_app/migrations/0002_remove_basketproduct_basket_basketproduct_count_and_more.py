# Generated by Django 4.1.7 on 2023-03-09 11:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('basket_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketproduct',
            name='basket',
        ),
        migrations.AddField(
            model_name='basketproduct',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='Count'),
        ),
        migrations.AddField(
            model_name='basketproduct',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='Ordered'),
        ),
        migrations.AddField(
            model_name='basketproduct',
            name='session_key',
            field=models.ForeignKey(default='afsd', on_delete=django.db.models.deletion.PROTECT, related_name='session_keys', to='sessions.session'),
        ),
        migrations.AddField(
            model_name='basketproduct',
            name='total_price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Total price'),
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
    ]