# Generated by Django 3.0.6 on 2020-05-07 08:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_software', '0011_software_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
