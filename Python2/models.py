# -*- coding: utf-8 -*-

class Perfil(object):
	'Classe padrão para perfis de usuarios'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas += 1

	def devolve_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []

		for linha in arquivo:
			valores = linha.split(',')
			perfis.append(classe(*valores))

		arquivo.close()

		return perfis

class Perfil_Vip(Perfil):
	'Classe padrão para perfis de usuários VIPs'

	def __init__(self, nome, telefone, empresa, apelido = ''):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def devolve_creditos(self):
		return super(Perfil_Vip, self).devolve_curtidas() * 10.0