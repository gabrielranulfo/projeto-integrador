# Generated by Django 4.1.2 on 2022-11-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_cad_empresa_cep_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad_setores',
            name='cargo_setor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_setores',
            name='contato_setor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_setores',
            name='resposavel_setor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_setores',
            name='setor_nome',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]