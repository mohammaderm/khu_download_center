# Generated by Django 3.0.6 on 2020-05-23 13:05

import app_account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0006_auto_20200523_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default-avatar.jpg', null=True, upload_to=app_account.models.image_path),
        ),
    ]