# Generated by Django 3.1.12 on 2022-10-18 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurantName',
            new_name='restaurant_name',
        ),
    ]
