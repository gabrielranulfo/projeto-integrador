# Generated by Django 2.1.15 on 2021-10-31 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cad_dados_previos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_itens_auditaveis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.CharField(max_length=90)),
                ('il', models.IntegerField(max_length=4)),
                ('icn', models.IntegerField(max_length=4)),
                ('e', models.IntegerField(max_length=4)),
            ],
        ),
    ]
