# Generated by Django 3.0.6 on 2020-05-11 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0004_bookmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cumment',
            old_name='values',
            new_name='value',
        ),
    ]