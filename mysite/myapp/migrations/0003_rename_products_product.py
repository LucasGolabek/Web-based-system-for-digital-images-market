# Generated by Django 4.0.4 on 2022-11-09 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_products_delete_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]