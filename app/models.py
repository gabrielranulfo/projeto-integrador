# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
#from django.contrib.auth.models import User


class Cad_empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome_fantasia_empresa = models.CharField(max_length=80,blank=False,null=False)
    cnpj_empresa = models.CharField(max_length=18,blank=True,null=True)
    endereco_empresa = models.CharField(max_length=80,blank=True,null=True)
    cidade_empresa = models.CharField(max_length=80,blank=True,null=True)
    cep_empresa = models.CharField(max_length=9,blank=True,null=True)
    estado_empresa = models.CharField(max_length=40,blank=True,null=True)
    telefone_empresa = models.CharField(max_length=15,blank=True,null=True)
    class Meta:
        verbose_name = 'Cadastro de Empresa'
    def __str__(self):
        return self.nome_fantasia_empresa

from django.db.models import Count
class Cad_setores(models.Model):
    id = models.AutoField(primary_key=True)
    setor_nome = models.CharField(max_length=30)
    resposavel_setor = models.CharField(max_length=30)
    cargo_setor = models.CharField(max_length=30)
    contato_setor = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Cadastro de Setores'
    def __str__(self):
        return self.setor_nome


class Cad_equipes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30,blank=False,null=False)
    telefone = models.CharField(max_length=30,blank=True,null=True)
    responsabilidade = models.CharField(max_length=30,blank=True,null=True)
    class Meta:
        verbose_name = 'Cadastro de Equipe'
    def __str__(self):
        return self.nome

class Cad_fornecedores(models.Model):
    id = models.AutoField(primary_key=True)
    fornecedor = models.CharField(max_length=30,blank=False,null=False)
    cnpj = models.CharField(max_length=30,blank=True,null=True)
    dpo = models.CharField(max_length=30,blank=True,null=True)
    telefone = models.CharField(max_length=30,blank=True,null=True)
    class Meta:
        verbose_name = 'Cadastro de Fornecedores'
    def __str__(self):
        return self.fornecedor

class Cad_dpo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30,blank=False,null=False)
    cpf = models.CharField(max_length=30,blank=True,null=True)
    cargo = models.CharField(max_length=30,blank=True,null=True)
    contato = models.CharField(max_length=30,blank=True,null=True)
    empresa = models.CharField(max_length=30,blank=True,null=True)
    cnpj = models.CharField(max_length=30,blank=True,null=True)
    endereco = models.CharField(max_length=30,blank=True,null=True)
    cidade = models.CharField(max_length=30,blank=True,null=True)
    estado = models.CharField(max_length=30,blank=True,null=True)
    class Meta:
        verbose_name = 'Cadastro de DPO'
    def __str__(self):
        return self.nome

class Cad_dados_previos(models.Model):
    RES_CHOICES = (
        ("S","SIM"),
        ("N","NÃO")
    )
    id = models.AutoField(primary_key=True)
    questao_dados_previos = models.CharField(max_length=90)
    resposta = models.CharField(max_length=10,choices=RES_CHOICES,blank=False,null=False)
    class Meta:
        verbose_name = 'Dados Prévio'
    def __str__(self):
        return self.questao_dados_previos

class Cad_itens_auditaveis(models.Model):
    INDICES = (
        (1,"BAIXO"),
        (2,"NORMAL"),
        (3,"MEDIO"),
        (4,"ALTO"),
        (5,"MUITO ALTO"),

    )
    EVIDENCIA = (
        (1,"SIM"),
        (0,"NÃO")
    )
    id = models.AutoField(primary_key=True)
    questao_itens_auditaveis = models.CharField(max_length=90,blank=False,null=False)
    il = models.IntegerField(blank=False,choices=INDICES,null=False)
    icn = models.IntegerField(blank=False,choices=INDICES,null=False)
    e = models.IntegerField(blank=False,choices=EVIDENCIA,null=False)
    fr = models.IntegerField(blank=False,null=False)

    @property
    def fr(self):
        return (self.il ** 2 + self.icn ** 2)*((7-self.e) ** 2) 
    
    class Meta:
        verbose_name = 'Cadastro de Itens Auditaveis'
    def __str__(self):
        return self.questao_itens_auditaveis

    
class Cad_fator_de_risco(models.Model):
    id = models.AutoField(primary_key=True)
    questao_fator_de_risco = models.CharField(max_length=90,blank=False,null=False)
    fator_de_risco = models.IntegerField(blank=False,null=False)
    #fator_de_risco = Cad_itens_auditaveis.fr()
    ##CALCULO DO FATOR DE RISCO fr = (il ** 2 + icn ** 2)*((7-e) ** 2) 

class Cad_Mapeamento(models.Model):
    UM_A_CINCO_CHOICES = (
        ("1" ,"1"),
        ("2" ,"2"),
        ("3" ,"3"),
        ("4" ,"4"),
        ("5" ,"5"),
    )
    SIM_OU_NAO_CHOICES = (
        ("S","SIM"),
        ("N","NÃO"),
    )
    BASES_LEGAIS = (
        ("Consentimento do titular","Consentimento do titular"),
        ("Legítimo interesse","Legítimo interesse"),
        ("Cumprimento de obrigação legal ou regulatória","Cumprimento de obrigação legal ou regulatória"),
        ("Tratamento pela administração pública","Tratamento pela administração pública"),
        ("Realização de estudos e de pesquisa","Realização de estudos e de pesquisa"),
        ("Execução ou preparação contratual","Execução ou preparação contratual"),
        ("Exercício regular de direitos","Exercício regular de direitos"),
        ("Proteção da vida e da incolumidade física","Proteção da vida e da incolumidade física"),
        ("Tutela de saúde do titular","Tutela de saúde do titular"),
        ("Proteção de crédito","Proteção de crédito")
    )
    TIPOS_DE_DADOS = (
        ("Dado Pessoal","Dado Pessoal"),
        ("Dado Sensível","Dado Sensível"),
        ("Dado Público","Dado Público"),
        ("Dado Anonimizado","Dado Anonimizado")

    )
    id = models.AutoField(primary_key=True)
    dado = models.CharField(max_length=30,blank=False,null=False)
    tipo = models.CharField(max_length=30,choices=TIPOS_DE_DADOS,blank=True,null=True)
    fonte = models.CharField(max_length=30,blank=True,null=True)
    motivo = models.CharField(max_length=30,blank=True,null=True)
    base_legal = models.CharField(max_length=45,choices=BASES_LEGAIS,blank=True,null=True)
    tratamento = models.CharField(max_length=30,blank=True,null=True)
    eliminacao = models.CharField(max_length=30,blank=True,null=True)
    compartilhamento = models.CharField(max_length=30,choices=SIM_OU_NAO_CHOICES,blank=True,null=True)
    necessario_consentimento = models.CharField(max_length=30,choices=SIM_OU_NAO_CHOICES,blank=True,null=True)
    possui_consentimento = models.CharField(max_length=30,choices=SIM_OU_NAO_CHOICES,blank=True,null=True)
    menor = models.CharField(max_length=30,choices=SIM_OU_NAO_CHOICES,blank=True,null=True)
    impacto_pessoal = models.CharField(max_length=30,choices=UM_A_CINCO_CHOICES,blank=True,null=True)
    missao_critica = models.CharField(max_length=30,choices=UM_A_CINCO_CHOICES,blank=True,null=True)
    class Meta:
        verbose_name = 'Mapeamento de Dado'
    def __str__(self):
        return self.dado