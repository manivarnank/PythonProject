# Generated by Django 3.2.12 on 2022-03-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-05-28'),
            preserve_default=False,
        ),
    ]
