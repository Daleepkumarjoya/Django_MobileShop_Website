# Generated by Django 4.1.2 on 2023-12-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0014_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='OrderId',
            field=models.IntegerField(default=None),
        ),
    ]
