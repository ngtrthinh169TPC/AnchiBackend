# Generated by Django 3.2 on 2022-11-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20221103_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default='fallback.png', upload_to='images/foods'),
        ),
    ]
