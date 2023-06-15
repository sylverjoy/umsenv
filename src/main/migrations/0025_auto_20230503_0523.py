# Generated by Django 3.1.7 on 2023-05-03 04:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20230428_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('deg_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('total_credits', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterSession',
            fields=[
                ('session', models.CharField(max_length=9)),
                ('semester', models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2')], max_length=200)),
                ('ss_id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('semester_start', models.DateField(default=datetime.datetime(2023, 5, 3, 5, 23, 28, 754351))),
                ('semester_end', models.DateField(default=datetime.datetime(2023, 5, 3, 5, 23, 28, 754351))),
                ('ca_deadline', models.DateField(default=datetime.datetime(2023, 5, 3, 5, 23, 28, 754351))),
                ('active', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='attendence',
        ),
        migrations.RemoveField(
            model_name='result',
            name='dept',
        ),
        migrations.AlterField(
            model_name='dept',
            name='dept_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='level',
            field=models.CharField(choices=[('HND1', 'HND1'), ('HND2', 'HND2'), ('BTECH', 'BTECH')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='AssignedTeacher',
        ),
        migrations.AddField(
            model_name='dept',
            name='school',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.school'),
        ),
        migrations.AddField(
            model_name='result',
            name='sem_ses',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.semestersession'),
        ),
        migrations.AddField(
            model_name='student',
            name='degree_pursued',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.degree'),
        ),
    ]