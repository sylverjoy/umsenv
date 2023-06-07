# Generated by Django 3.1.7 on 2023-06-05 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20230515_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='level',
            field=models.CharField(default='HND1', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='ca_deadline',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 6, 50, 40, 923413)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_end',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 6, 50, 40, 923413)),
        ),
        migrations.AlterField(
            model_name='semestersession',
            name='semester_start',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 6, 50, 40, 923413)),
        ),
    ]
