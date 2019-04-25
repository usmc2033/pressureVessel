# Generated by Django 2.1.2 on 2019-04-07 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_remove_component_material'),
        ('reporter', '0022_auto_20190407_1119'),
        ('state', '0003_headstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiftingLugState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('W', models.FloatField(default=0.0)),
                ('phi', models.FloatField(default=0.0)),
                ('x_1', models.FloatField(default=0.0)),
                ('x_2', models.FloatField(default=0.0)),
                ('F_r', models.FloatField(default=0.0)),
                ('d_reqd', models.FloatField(default=0.0)),
                ('diameter_ratio', models.FloatField(default=0.0)),
                ('D_p', models.FloatField(default=0.0)),
                ('sigma_sd_calc', models.FloatField(default=0.0)),
                ('sigma_sd_ratio', models.FloatField(default=0.0)),
                ('t_reqd_tensile', models.FloatField(default=0.0)),
                ('L', models.FloatField(default=0.0)),
                ('d', models.FloatField(default=0.0)),
                ('sigma_t', models.FloatField(default=0.0)),
                ('sigma_t_calc', models.FloatField(default=0.0)),
                ('sigma_t_ratio', models.FloatField(default=0.0)),
                ('t', models.FloatField(default=0.0)),
                ('t_reqd_bearing', models.FloatField(default=0.0)),
                ('A_bearing', models.FloatField(default=0.0)),
                ('sigma_b_calc', models.FloatField(default=0.0)),
                ('sigma_b_ratio', models.FloatField(default=0.0)),
                ('phi_shear', models.FloatField(default=0.0)),
                ('L_shear', models.FloatField(default=0.0)),
                ('H', models.FloatField(default=0.0)),
                ('a_2', models.FloatField(default=0.0)),
                ('t_reqd_shear', models.FloatField(default=0.0)),
                ('t_max', models.FloatField(default=0.0)),
                ('thickness_ratio', models.FloatField(default=0.0)),
                ('A_shear', models.FloatField(default=0.0)),
                ('tau', models.FloatField(default=0.0)),
                ('sigma_s', models.FloatField(default=0.0)),
                ('sigma_s_ratio', models.FloatField(default=0.0)),
                ('A_weld', models.FloatField(default=0.0)),
                ('t_w', models.FloatField(default=0.0)),
                ('alpha', models.FloatField(default=0.0)),
                ('tau_t', models.FloatField(default=0.0)),
                ('tau_s', models.FloatField(default=0.0)),
                ('M', models.FloatField(default=0.0)),
                ('Hght', models.FloatField(default=0.0)),
                ('c', models.FloatField(default=0.0)),
                ('h', models.FloatField(default=0.0)),
                ('l', models.FloatField(default=0.0)),
                ('tau_b', models.FloatField(default=0.0)),
                ('tau_allowable', models.FloatField(default=0.0)),
                ('tau_ratio', models.FloatField(default=0.0)),
                ('lug_pin_check', models.BooleanField(default=False)),
                ('lug_thickness_check', models.BooleanField(default=False)),
                ('shear_thickness_check', models.BooleanField(default=False)),
                ('shear_diameter_check', models.BooleanField(default=False)),
                ('tensile_check', models.BooleanField(default=False)),
                ('bearing_check', models.BooleanField(default=False)),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='component.Component')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Report', verbose_name='the related report')),
            ],
        ),
        migrations.CreateModel(
            name='SkirtState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_skirt', models.CharField(max_length=255)),
                ('thickness', models.FloatField(default=0.0)),
                ('corrosion_allowance', models.FloatField(default=0.0)),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='component.Component')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Report', verbose_name='the related report')),
            ],
        ),
    ]
