# Generated by Django 2.2.5 on 2020-11-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hour', '0006_auto_20201113_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absenteeismrate',
            name='absenteeism',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Absenteeism'),
        ),
    ]