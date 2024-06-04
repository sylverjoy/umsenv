# Generated by Django 3.1.7 on 2024-05-20 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20240420_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(default='3'),
        ),
        migrations.AlterField(
            model_name='result',
            name='term_test',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='term_test_resit',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='theory_marks',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline_btech',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline_masters',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline_btech',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline_masters',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_end',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_start',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 15, 27, 11, 403389)),
        ),
    ]
