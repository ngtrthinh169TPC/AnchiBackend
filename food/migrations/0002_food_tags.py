# Generated by Django 3.1.12 on 2022-10-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
    ]