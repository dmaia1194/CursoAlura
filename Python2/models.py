# -*- coding: utf-8 -*-

class Perfil(object):
	'Classe para moldar perfis de usuarios'

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

class Perfil_Vip(Perfil):
	'Classe padrão para perfis de usuários VIPs'

	def devolve_creditos(self):
		return super(Perfil_Vip, self).devolve_curtidas() * 10.0