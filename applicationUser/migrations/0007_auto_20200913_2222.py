# Generated by Django 3.1.1 on 2020-09-14 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationUser', '0006_auto_20200913_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
