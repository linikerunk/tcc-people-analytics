# Generated by Django 2.2.5 on 2020-09-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_remove_training_training_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='category',
            field=models.CharField(choices=[('Tecnologia da informação', 'Tecnologia da informação'), ('Treinamento online', 'Treinamento online'), ('Programas de mentoria', 'Programas de mentoria'), ('Coaching empresarial', 'Coaching empresarial'), ('Workshops', 'Workshops'), ('Gestão do conhecimento', 'Gestão do conhecimento'), ('Treinamento presencial com instrutor', 'Treinamento presencial com instrutor'), ('Treinamento de desenvolvimento de Soft Skills', 'Treinamento de desenvolvimento de Soft Skills'), ('Treinamentos obrigatórios', 'Treinamentos obrigatórios')], max_length=50, verbose_name='Categoria'),
        ),
    ]
