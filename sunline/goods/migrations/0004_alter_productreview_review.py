# Generated by Django 4.2.7 on 2024-02-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_products_user_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
