# Generated by Django 3.0.3 on 2020-03-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0008_auto_20200304_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='currentSpending',
            field=models.ManyToManyField(blank=True, to='goals.Spending'),
        ),
    ]