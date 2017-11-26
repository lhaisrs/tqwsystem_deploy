from abc import ABC, abstractmethod

class IAnalisador(ABC):

	@abstractmethod
	def gerarRelatorio(self, formularios):
		pass

	@abstractmethod
	def gerarRelatorioTeste(self):
		pass