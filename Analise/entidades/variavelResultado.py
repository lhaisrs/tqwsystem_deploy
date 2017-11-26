class VariavelResultado(object):
	nome = None
	alfa = 0
	media = 0.0
	desvioPadrao = 0.0
	correlacoes = []

	def __init__(self, nome, alfa, media, desvioPadrao, correlacoes):
		self.nome = nome
		self.alfa = alfa	
		self.media = media
		self.desvioPadrao = desvioPadrao
		self.correlacoes = correlacoes

	def getCorrelacaoPorNome(self, variavel):
		for v in self.correlacoes:
			if v.nomeVariavel == variavel:
				return v.valor
		return None

	def getCorrelacao(self, idVariavel):
		return self.correlacoes[idVariavel].valor

	def __str__(self):
		return "Nome: " + self.nome.__str__() + " Media: " + self.media.__str__() + " Desvio: " + self.desvioPadrao.__str__() + "\nCorrelacoes: " + self.correlacoes.__str__() + "\n"