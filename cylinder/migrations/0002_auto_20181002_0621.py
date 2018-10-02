# Generated by Django 2.1.1 on 2018-10-02 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cylinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='name',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='strength',
            field=models.FloatField(default=0),
        ),
    ]
