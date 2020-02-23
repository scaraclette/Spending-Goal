# Generated by Django 3.0.3 on 2020-02-23 01:13

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='checkAmount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=14),
        ),
        migrations.AlterField(
            model_name='goal',
            name='needToSpend',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=14),
        ),
        migrations.AlterField(
            model_name='goal',
            name='percentGoal',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=14),
        ),
        migrations.AlterField(
            model_name='spending',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=14),
        ),
    ]
