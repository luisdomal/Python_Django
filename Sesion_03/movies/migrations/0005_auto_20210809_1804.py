# Generated by Django 3.2.6 on 2021-08-09 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210809_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='writer',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='writer',
            old_name='writer',
            new_name='name',
        ),
    ]