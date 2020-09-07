# Generated by Django 2.2.5 on 2020-09-07 22:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20200903_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyMassIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now_add=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('weighing_date', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='Data Pesagem')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Peso')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura')),
                ('abdominal_circumference', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Circunferência Abdominal(cm)')),
                ('systolic_blood_pressure', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Pressão Arterial Sistólica')),
                ('diastolic_blood_pressure', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Pressão Arterial Diastólica')),
                ('classification', models.CharField(choices=[('Verde', 'Verde'), ('Amarelo', 'Amarelo'), ('Vermelho', 'Vermelho'), ('Azul', 'Azul')], max_length=8, verbose_name='Classificação')),
                ('classification_text', models.CharField(choices=[('Magreza grave', 'Magreza grave'), ('Magreza moderada', 'Magreza moderada'), ('Magreza leve', 'Magreza leve'), ('Saudável', 'Saudável'), ('Sobrepeso', 'Sobrepeso'), ('Obesidade Grau I', 'Obesidade Grau I'), ('Obesidade Grau II (severa)', 'Obesidade Grau II (severa)'), ('Obesidade Grau III (mórbida)', 'Obesidade Grau III (mórbida)')], max_length=28, verbose_name='Classificação IMC')),
                ('imc', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='IMC')),
                ('identifier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee', to='users.Employee')),
            ],
            options={
                'verbose_name': 'Indice de Massa Corporal',
                'verbose_name_plural': 'Indice de Massa Corporal',
            },
        ),
    ]
