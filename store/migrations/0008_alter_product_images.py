# Generated by Django 4.0.2 on 2022-03-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_descriptionin_arabic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='', verbose_name='الصوره'),
        ),
    ]
