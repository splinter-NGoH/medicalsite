# Generated by Django 4.0.2 on 2022-03-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0, verbose_name='السعر'),
            preserve_default=False,
        ),
    ]
