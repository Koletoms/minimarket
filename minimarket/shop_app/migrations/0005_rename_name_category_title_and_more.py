# Generated by Django 4.1.7 on 2023-03-07 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_subcategory_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='description',
        ),
    ]
