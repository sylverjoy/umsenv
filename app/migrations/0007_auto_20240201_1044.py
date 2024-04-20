# Generated by Django 3.1.7 on 2024-02-01 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230814_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline_btech',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline_masters',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline_btech',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline_masters',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_end',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_start',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 10, 44, 3, 887026)),
        ),
    ]
