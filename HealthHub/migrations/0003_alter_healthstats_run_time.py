# Generated by Django 3.2.15 on 2022-09-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthHub', '0002_auto_20220921_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthstats',
            name='run_time',
            field=models.DurationField(),
        ),
    ]
