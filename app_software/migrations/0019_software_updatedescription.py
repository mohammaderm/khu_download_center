# Generated by Django 3.0.6 on 2020-05-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_software', '0018_software_countercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='updatedescription',
            field=models.CharField(blank=True, default='اطلاعات توسط ادمین ثبت نشده است.', max_length=500, null=True),
        ),
    ]
