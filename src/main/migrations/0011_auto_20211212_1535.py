# Generated by Django 3.1.7 on 2021-12-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211212_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(default='0', max_length=1),
        ),
    ]