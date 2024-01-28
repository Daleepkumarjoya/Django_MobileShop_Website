# Generated by Django 4.1.2 on 2023-11-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Image', models.ImageField(upload_to='images')),
                ('Product_Name', models.CharField(max_length=200)),
                ('Product_Price', models.IntegerField(default=0)),
                ('Product_Desc', models.TextField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
