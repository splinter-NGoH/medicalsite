# Generated by Django 4.0.2 on 2022-03-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(blank=True, verbose_name='السعر'),
        ),
    ]
