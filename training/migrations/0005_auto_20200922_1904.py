# Generated by Django 2.2.5 on 2020-09-22 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20200922_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='present_list',
            field=models.FileField(blank=True, default='', null=True, upload_to='present_list', verbose_name='Lista de Presença'),
        ),
    ]