# Generated by Django 4.0.2 on 2022-09-23 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopsdetail', '0003_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shopsdetail.groups')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shopsdetail.categories')),
            ],
        ),
    ]