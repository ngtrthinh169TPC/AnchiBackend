# Generated by Django 3.2 on 2022-11-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0004_ingredient_description'),
        ('tag', '0004_tag_description'),
        ('food', '0006_auto_20221103_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='ingredient.Ingredient'),
        ),
        migrations.AlterField(
            model_name='food',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tag.Tag'),
        ),
    ]
