# Generated by Django 3.0.5 on 2020-05-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_software', '0010_file_software_title_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='version',
            field=models.CharField(max_length=100, null=True),
        ),
    ]