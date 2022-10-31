# Generated by Django 3.1.12 on 2022-10-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('foodName', models.CharField(max_length=256, unique=True)),
                ('description', models.CharField(max_length=1024)),
                ('address', models.CharField(max_length=1024)),
                ('recipe', models.CharField(max_length=4096)),
            ],
        ),
    ]