# Generated by Django 4.0.2 on 2022-09-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shopsdetail', '0004_categories_subcategories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Groups',
            new_name='Shopgroup',
        ),
    ]
