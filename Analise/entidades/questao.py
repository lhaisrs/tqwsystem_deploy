class Questao(object):
	pergunta = None
	invertido = False
	resposta = 0

	def __init__(self, pergunta, invertido, resposta):
		self.pergunta = pergunta
		self.invertido = invertido
		self.resposta = resposta
