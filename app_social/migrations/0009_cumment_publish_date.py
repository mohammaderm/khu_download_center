# Generated by Django 3.0.6 on 2020-05-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0008_cumment_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='cumment',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]