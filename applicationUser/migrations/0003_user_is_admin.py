# Generated by Django 3.1.1 on 2020-09-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationUser', '0002_auto_20200912_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
