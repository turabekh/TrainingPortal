# Generated by Django 3.1.1 on 2020-09-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_learningobjective_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time_to_finish',
            field=models.IntegerField(default=0),
        ),
    ]