# Generated by Django 2.0.12 on 2019-12-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price_large',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='price_small',
            field=models.FloatField(default=0),
        ),
    ]
