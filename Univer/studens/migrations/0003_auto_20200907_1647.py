# Generated by Django 3.1.1 on 2020-09-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studens', '0002_education_facultet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='facultet',
            field=models.CharField(max_length=60, verbose_name='Факультет'),
        ),
    ]
