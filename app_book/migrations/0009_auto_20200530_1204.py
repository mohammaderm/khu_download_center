# Generated by Django 3.0.6 on 2020-05-30 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_book', '0008_auto_20200530_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_book.Book'),
        ),
    ]
