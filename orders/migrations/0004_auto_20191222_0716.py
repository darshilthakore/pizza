# Generated by Django 2.0.12 on 2019-12-22 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191220_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
