# Generated by Django 4.0.2 on 2022-03-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_homesliedes_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='صوره لو في'),
        ),
        migrations.AlterField(
            model_name='homesliedes',
            name='slide_image',
            field=models.ImageField(upload_to='', verbose_name='صوره'),
        ),
    ]
