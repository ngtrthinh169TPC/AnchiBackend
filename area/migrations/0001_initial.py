# Generated by Django 3.2 on 2022-11-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
