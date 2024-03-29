# Generated by Django 4.2.7 on 2024-02-19 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_categories_image'),
        ('main', '0004_featuredproducts_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewArrivals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='new_arrivals_images')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('group', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories')),
            ],
            options={
                'db_table': 'new arrivals products',
                'ordering': ('id',),
            },
        ),
    ]
