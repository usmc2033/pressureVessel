# Generated by Django 2.1.2 on 2019-02-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0009_auto_20190225_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='cylinderstate',
            name='t_inter',
            field=models.FloatField(default=0.0),
        ),
    ]
