# Generated by Django 2.1.15 on 2021-10-31 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_cad_equipes_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_dados_previos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.CharField(max_length=90)),
                ('resposta', models.CharField(max_length=10)),
            ],
        ),
    ]
