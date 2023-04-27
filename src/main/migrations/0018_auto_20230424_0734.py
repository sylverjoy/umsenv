# Generated by Django 3.1.7 on 2023-04-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20230423_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertable',
            name='status',
            field=models.CharField(default='Approved', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('L1', 'HND1'), ('L2', 'HND2'), ('L3', 'BTECH')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='level',
            field=models.CharField(choices=[('L1', 'HND1'), ('L2', 'HND2'), ('L3', 'BTECH')], max_length=200, null=True),
        ),
    ]