# -*- coding: UTF-8 -*-

def cadastrar(nomes):
	print 'Digite o nome:'

	nome = raw_input()
	nomes.append(nome)

def menu():
	nomes = []
	escolha = ''

	while(escolha!='0'):
		print 'Digite: 1 para cadastrar, 0 para terminar'

		escolha = raw_input()
		if(escolha=='1'):
			cadastrar(nomes)

menu()