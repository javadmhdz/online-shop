# Generated by Django 5.1.1 on 2024-09-14 07:45

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 14, 11, 15, 2, 294812)),
        ),
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]