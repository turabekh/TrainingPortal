# Generated by Django 3.1.1 on 2020-09-13 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_learningobjective_teacher'),
        ('lessons', '0006_step_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]