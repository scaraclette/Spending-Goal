# Generated by Django 3.0.3 on 2020-02-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20200223_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='ntsDuration',
            field=models.CharField(max_length=21, null=True),
        ),
    ]