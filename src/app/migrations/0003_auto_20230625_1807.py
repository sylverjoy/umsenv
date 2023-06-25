# Generated by Django 3.1.7 on 2023-06-25 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230625_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='dep',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline',
            field=models.DateField(default=datetime.datetime(2023, 6, 25, 18, 7, 26, 956939)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline_btech',
            field=models.DateField(default=datetime.datetime(2023, 6, 25, 18, 7, 26, 956939)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline',
            field=models.DateField(default=datetime.datetime(2023, 6, 25, 18, 7, 26, 956939)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline_btech',
            field=models.DateField(default=datetime.datetime(2023, 6, 25, 18, 7, 26, 956939)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_end',
            field=models.DateField(default=datetime.datetime(2023, 6, 25, 18, 7, 26, 956939)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_start',
            field=models.DateField(default=datetime.datetime(2023, 6, 25, 18, 7, 26, 956939)),
        ),
    ]