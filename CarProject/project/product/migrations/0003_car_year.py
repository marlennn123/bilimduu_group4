# Generated by Django 4.2.8 on 2024-04-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_car_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
