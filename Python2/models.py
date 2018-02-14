# -*- coding: utf-8 -*-

class Perfil(object):
	'Classe para moldar perfis de usuarios'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.curtidas = 0

	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)