# Generated by Django 4.0.2 on 2022-08-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_product_name_in_arabic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name_in_arabic',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='اسم المنتج بالعربي'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name_in_inglish',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='اسم المنتج بالانجليزي'),
        ),
    ]
