# Generated by Django 2.1.2 on 2019-02-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0006_auto_20190217_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='location',
        ),
    ]
