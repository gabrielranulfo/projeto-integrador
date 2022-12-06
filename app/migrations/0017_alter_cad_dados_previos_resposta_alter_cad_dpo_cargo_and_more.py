# Generated by Django 4.1.2 on 2022-11-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_cad_fornecedores_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad_dados_previos',
            name='resposta',
            field=models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=10),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='cargo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='cidade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='cnpj',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='contato',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='cpf',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='empresa',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='endereco',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_dpo',
            name='estado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_equipes',
            name='responsabilidade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_equipes',
            name='telefone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_fornecedores',
            name='cnpj',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_fornecedores',
            name='dpo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_fornecedores',
            name='telefone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='base_legal',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='compartilhamento',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='dado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='eliminacao',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='fonte',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='impacto_pessoal',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='menor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='missao_critica',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='motivo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='necessario_consentimento',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='possui_consentimento',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cad_mapeamento',
            name='tratamento',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]