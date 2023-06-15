# Generated by Django 3.1.7 on 2023-06-08 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20230607_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='UBa_Mentor_School',
            field=models.CharField(default='Faculty of Economics and Management Sciences (FEMS)', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 8, 19, 6, 203411)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline_btech',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 8, 19, 6, 203411)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 8, 19, 6, 203411)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='result_deadline_btech',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 8, 19, 6, 203411)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_end',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 8, 19, 6, 203411)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_start',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 8, 19, 6, 203411)),
        ),
    ]