# Generated by Django 4.2.7 on 2024-03-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_newarrivals_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestselling',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
    ]
