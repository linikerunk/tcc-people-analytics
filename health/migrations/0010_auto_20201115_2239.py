# Generated by Django 2.2.5 on 2020-11-16 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_auto_20201024_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymassindex',
            name='classification',
            field=models.CharField(blank=True, choices=[('Verde', 'Saudável'), ('Amarelo', 'Sedentário'), ('Vermelho', 'Precisa de Acompanhamento Médico'), ('Azul', 'Risco de Morte')], max_length=8, verbose_name='Classificação'),
        ),
    ]
