# Generated by Django 4.1.7 on 2023-03-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='payment', to='order_app.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]