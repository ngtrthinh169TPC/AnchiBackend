# Generated by Django 3.1.12 on 2022-10-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.AutoField(primary_key=True, serialize=False)),
                ('restaurantName', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=1024)),
                ('menu', models.CharField(max_length=4096)),
                ('note', models.CharField(max_length=1024)),
            ],
        ),
    ]
