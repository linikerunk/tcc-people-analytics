# Generated by Django 2.2.5 on 2020-10-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201003_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('N/A', 'N/A')], max_length=12, verbose_name='Gênero'),
        ),
    ]
