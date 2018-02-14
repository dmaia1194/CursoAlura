def gera_nome_convite(convite):
	posicao_final = len(convite)
	posicao_inicial = posicao_final - 4

	parte1 = convite[0:4]
	parte2 = convite[posicao_inicial:posicao_final]

	return parte1 + ' ' + parte2

def envia_convite(nome_formatado):
	print 'Enviando convite para %s' % (nome_formatado)

def processa_convite(convite):
	nome_formatado = gera_nome_convite(convite)
	envia_convite(nome_formatado)

def cadastrar(nomes):
	print 'Digite o nome:'

	nome = raw_input()
	nomes.append(nome)

def remover(nomes):
	print 'Qual nome voce gostaria de remover?'

	nome = raw_input()
	nomes.remove(nome)