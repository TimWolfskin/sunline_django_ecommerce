# Generated by Django 4.2.7 on 2024-03-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_bestselling'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeaturedProducts',
        ),
    ]