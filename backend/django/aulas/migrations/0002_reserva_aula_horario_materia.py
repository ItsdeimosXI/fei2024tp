# Generated by Django 5.0.6 on 2024-05-28 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reserva_aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fh_desde', models.TimeField()),
                ('fh_hasta', models.TimeField()),
                ('observaciones', models.TextField(max_length=256)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.aula')),
            ],
        ),
        migrations.CreateModel(
            name='horario_materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fh_desde', models.TimeField()),
                ('fh_hasta', models.TimeField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.materia')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.reserva_aula')),
            ],
        ),
    ]