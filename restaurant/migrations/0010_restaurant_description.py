# Generated by Django 3.2 on 2022-11-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_restaurant_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]