# Generated by Django 4.2.7 on 2024-03-10 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_remove_products_returns_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_return',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_shipping',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
