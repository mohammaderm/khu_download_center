# Generated by Django 3.0.5 on 2020-05-02 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_software', '0004_software_tutorial_install'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download_link',
            name='object_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_software.Software'),
        ),
    ]
