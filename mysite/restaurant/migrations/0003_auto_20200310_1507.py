# Generated by Django 3.0.3 on 2020-03-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurantfood_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='close_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='open_time',
            field=models.TimeField(),
        ),
    ]
