# Generated by Django 5.1.7 on 2025-03-23 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaManutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('TVM', 'Trocar valvula do motor'), ('TO', 'Troca de óleo'), ('TOB', 'Trocar óleo da bengala'), ('TB', 'Trocar bateria'), ('TF', 'Trocar filtros'), ('TP', 'Trocar pneu'), ('TS', 'Trocar sela')], max_length=3)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('data_inicio', models.DateField(null=True)),
                ('data_entrega', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('protocolo', models.CharField(blank=True, max_length=32, null=True)),
                ('categoria_manutencao', models.ManyToManyField(to='servicos.categoriamanutencao')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente')),
            ],
        ),
    ]
