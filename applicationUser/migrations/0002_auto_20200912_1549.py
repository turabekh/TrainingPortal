# Generated by Django 3.1.1 on 2020-09-12 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicationUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
