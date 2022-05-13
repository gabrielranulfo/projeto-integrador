# Generated by Django 2.1.15 on 2021-10-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia_empresa', models.CharField(max_length=80)),
                ('cnpj_empresa', models.CharField(max_length=18)),
                ('endereco_empresa', models.CharField(max_length=80)),
                ('cidade_empresa', models.CharField(max_length=80)),
                ('cep_empresa', models.CharField(max_length=9)),
                ('estado_empresa', models.CharField(max_length=40)),
                ('telefone_empresa', models.CharField(max_length=15)),
            ],
        ),
    ]
