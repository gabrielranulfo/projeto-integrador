# Generated by Django 2.1.15 on 2021-10-31 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_cad_itens_auditaveis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad_itens_auditaveis',
            name='e',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cad_itens_auditaveis',
            name='icn',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cad_itens_auditaveis',
            name='il',
            field=models.IntegerField(),
        ),
    ]
