# Generated by Django 2.0.12 on 2019-12-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Waiting for Confirmation', max_length=64),
        ),
    ]
