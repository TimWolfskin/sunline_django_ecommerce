# Generated by Django 4.2.7 on 2024-02-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_newarrivals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newarrivals',
            name='group',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]