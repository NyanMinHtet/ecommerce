# Generated by Django 5.0.6 on 2024-06-09 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_can_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='category',
        ),
    ]