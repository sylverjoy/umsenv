# Generated by Django 3.1.7 on 2021-12-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_assignedteacher2'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
