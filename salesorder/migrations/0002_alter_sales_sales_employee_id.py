# Generated by Django 4.2.8 on 2024-01-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sales_employee_id',
            field=models.IntegerField(unique=True),
        ),
    ]