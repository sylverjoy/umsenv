# Generated by Django 3.1.7 on 2023-04-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20230428_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='0000.jpeg', null=True, upload_to=''),
        ),
    ]
