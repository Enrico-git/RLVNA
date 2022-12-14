# Generated by Django 4.0.4 on 2022-05-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_settings_experiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='data_frequency',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='num_controllers',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='topology',
            field=models.JSONField(),
        ),
    ]
