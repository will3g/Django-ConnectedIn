from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=12, null=False)
    nome_empresa = models.CharField(max_length=30, null=False)
    contatos = models.ManyToManyField('self')

    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()
#####################################################
# DE UMA MANEIRA SIMPLES E SEM SALVAR NO BD, FICARIA:
# class Perfil(object):
#
#   def __init__(self, nome='', email='', telefone='', nome_empresa=''):
#     self.nome = nome
#     self.email = email
#     self.telefone = telefone
#     self.nome_empresa = nome_empresa
