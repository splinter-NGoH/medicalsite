# Generated by Django 4.0.2 on 2022-03-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customerrequests'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrequests',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='ملحوظه'),
        ),
    ]
