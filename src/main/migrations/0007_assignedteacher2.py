# Generated by Django 3.1.7 on 2021-12-08 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211208_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedTeacher2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_dept', models.CharField(max_length=3)),
                ('course_code', models.CharField(max_length=200)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dept')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'unique_together': {('student_dept', 'course_code')},
            },
        ),
    ]