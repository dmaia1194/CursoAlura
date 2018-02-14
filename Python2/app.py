# -*- coding: UTF-8 -*-

def cadastrar(nomes):
	print 'Digite o nome:'

	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes:'

	for nome in nomes:
		print nome

def remover(nomes):
	print 'Qual nome gostaria de remover?'

	nome = raw_input()
	nomes.remove(nome)

def alterar(nomes):
	print 'Qual nome gostaria de alterar?'

	nome = raw_input()
	if nome in nomes:
		print 'Digite o novo nome:'
		
		novo_nome = raw_input()
		posicao = nomes.index(nome)
		nomes[posicao] = novo_nome

def procurar(nomes):
	print 'Digite o nome a procurar:'

	nome = raw_input()
	if nome in nomes:
		print 'Nome localizado'
	else:
		print 'Nome não existe'

def menu():
	nomes = []
	escolha = ''

	while escolha != '0':
		print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 0 para terminar'

		escolha = raw_input()
		if escolha == '1':
			cadastrar(nomes)
		if escolha == '2':
			listar(nomes)
		if escolha == '3':
			remover(nomes)
		if escolha == '4':
			alterar(nomes)
		if escolha == '5':
			procurar(nomes)

menu()