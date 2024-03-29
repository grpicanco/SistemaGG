# Generated by Django 3.0 on 2019-12-08 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('cidade', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=20)),
                ('logradouro', models.CharField(max_length=20)),
                ('grupo_responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('cpf', models.CharField(max_length=11)),
                ('escolaridade', models.PositiveSmallIntegerField(choices=[(1, 'Ensino Fundamental'), (2, 'Ensino Médio'), (3, 'Ensino Superior')])),
                ('data_nascimento', models.DateField()),
                ('profissao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('objetivo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabalha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Participa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Funcao')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Pessoa')),
            ],
        ),
    ]
