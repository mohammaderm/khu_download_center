# Generated by Django 3.0.6 on 2020-05-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_software', '0016_file_software_os_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='counterlike',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]