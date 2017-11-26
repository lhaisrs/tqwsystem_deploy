class CorrelacaoVariaveis(object):
	idVariavel = 0
	nomeVariavel = None
	valor = 0

	def __init__(self, idVariavel, nomeVariavel, valor):
		self.idVariavel = idVariavel
		self.nomeVariavel = nomeVariavel
		self.valor = valor

	def __str__(self):
		return "Nome: " + self.nomeVariavel + " Valor: " + self.valor.__str__()