# Generated by Django 3.1.1 on 2020-09-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationUser', '0007_auto_20200913_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]
