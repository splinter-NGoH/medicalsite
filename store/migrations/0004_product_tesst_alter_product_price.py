# Generated by Django 4.0.2 on 2022-03-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, default=0, max_length=245, verbose_name='السعر'),
        ),
    ]