# Generated by Django 4.0.2 on 2022-09-24 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopsdetail', '0008_alter_subcategories_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Shopsdetail.shop'),
        ),
    ]
