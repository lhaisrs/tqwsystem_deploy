class RelatorioResultado(object):

	nome = None
	dataInicial = None
	dataFinal = None
	constructos = []

	def __init__(self, nome, dataInicial, dataFinal, constructos):
		self.nome = nome
		self.dataInicial = dataInicial
		self.dataFinal = dataFinal
		self.constructos = constructos

	def __str__(self):
		resultado = "-- Nome: %s -- \n" % (self.nome)
		resultado += "Constructos: \n"
		for c in self.constructos:
			resultado += " -> %s \n" % (c.nome)
			resultado += " Variaveis: nome  media  desvio  alfa \n"
			for v in c.variaveis:
				resultado += "  - %s  %0.2f %0.2f %0.2f\n" % (v.nome, v.media, v.desvioPadrao, v.alfa)
		return resultado