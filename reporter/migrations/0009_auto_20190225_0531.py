# Generated by Django 2.1.2 on 2019-02-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0008_report_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.FilePathField(allow_folders=True, path='/home/calcgen2/pressureVessel/static/reports/'),
        ),
    ]
