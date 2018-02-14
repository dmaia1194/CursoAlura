# -*- coding: utf-8 -*-

class Perfil(object):
	'Classe para moldar perfis de usuarios'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa