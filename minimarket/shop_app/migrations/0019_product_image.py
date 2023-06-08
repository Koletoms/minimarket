# Generated by Django 4.1.7 on 2023-03-13 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0018_alter_review_author_alter_review_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='images/default/product_default.png', upload_to='images/products/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], verbose_name='Image'),
        ),
    ]
