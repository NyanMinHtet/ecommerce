# Generated by Django 5.0.6 on 2024-06-09 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('Phone', 'Phone'), ('Food', 'Food'), ('Clothes', 'Clothes')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('payment_method', models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('Bank Transfer', 'Bank Transfer')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='store.product')),
            ],
        ),
    ]
