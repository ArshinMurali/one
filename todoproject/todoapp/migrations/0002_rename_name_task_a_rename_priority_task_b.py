# Generated by Django 4.2.2 on 2023-08-01 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='priority',
            new_name='b',
        ),
    ]
