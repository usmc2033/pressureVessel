# Generated by Django 2.1.2 on 2019-02-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0007_remove_report_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='location',
            field=models.FilePathField(default='report.txt'),
            preserve_default=False,
        ),
    ]
