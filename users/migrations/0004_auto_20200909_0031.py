# Generated by Django 2.2.5 on 2020-09-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200903_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='andress',
            field=models.CharField(blank=True, max_length=200, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='employee',
            name='andress_number',
            field=models.CharField(blank=True, max_length=6, verbose_name='Número'),
        ),
    ]
