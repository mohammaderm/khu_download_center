# Generated by Django 3.0.6 on 2020-05-10 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0002_auto_20200510_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='values',
        ),
    ]
