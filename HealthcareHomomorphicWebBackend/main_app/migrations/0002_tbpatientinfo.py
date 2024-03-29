# Generated by Django 4.0.3 on 2023-04-22 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbPatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('heart_rate', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('mass', models.FloatField(blank=True, null=True)),
                ('suger_level', models.FloatField(blank=True, null=True)),
                ('hb_level', models.FloatField(blank=True, null=True)),
                ('wbc_count', models.FloatField(blank=True, null=True)),
                ('residual_volume', models.FloatField(blank=True, null=True)),
                ('vital_capcity', models.FloatField(blank=True, null=True)),
                ('body_temp', models.FloatField(blank=True, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
