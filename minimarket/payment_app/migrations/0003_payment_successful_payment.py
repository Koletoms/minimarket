# Generated by Django 4.1.7 on 2023-03-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0002_payment_code_payment_month_payment_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='successful_payment',
            field=models.BooleanField(default=False),
        ),
    ]