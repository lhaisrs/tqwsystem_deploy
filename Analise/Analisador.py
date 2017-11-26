import numpy as np

from Analise import IAnalisador
from Analise.entidades.formulario import Formulario
from Analise.entidades.variavel import Variavel
from Analise.entidades.questao import Questao
from Analise.entidades.relatorioResultado import RelatorioResultado
from Analise.entidades.constructo import Constructo
from Analise.entidades.variavelResultado import VariavelResultado
from Analise.entidades.correlacaoVariaveis import CorrelacaoVariaveis

from scipy.stats.stats import pearsonr

class Analisador(IAnalisador):

	def cronbachAlpha(self, itemscores):
		itemvars = itemscores.var(axis=0, ddof=1)	## TODO verificar se os eixos que estao sendo utilizados estao corretos
		tscores = itemscores.sum(axis=1)			## axis=0 e axis=1. Na implementacao original esta invertido,
		nitems = len(itemscores)					## mas esta gerando valores negativos para o Alfa
		alfa = nitems / (nitems-1) * (1 - itemvars.sum() / tscores.var(ddof=1))
		return alfa

	def calcularAlfaVariavies(self, questoes):
		alfas = []
		x,y = questoes.shape
		for i in range(0,y): # COLUNAS = PARA CADA VARIAVEL
			coluna = questoes[0:x, i]	
			variavelRespostas = np.empty(shape=(0,len(coluna[0].questoes)))
			for v in coluna:
				respostas = []
				for q in v.questoes:
					respostas.append(q.resposta)
				variavelRespostas = np.vstack([variavelRespostas, respostas])
			alfa = self.cronbachAlpha(variavelRespostas)
			alfas.append(alfa)
		return alfas

	def avaliarVariaveis(self, variaveis, mapeamentoVariaveis, constructos, alfas):
		media = np.mean(variaveis, axis=0)
		desvio = np.std(variaveis, axis=0)
		correlacao = np.corrcoef(variaveis, rowvar=False)
		
		for c in constructos:
			c.variaveis = []

		for v in range(0,variaveis.shape[1]):
			v_resultado = VariavelResultado(mapeamentoVariaveis[v][0], alfas[v], media[v], desvio[v], self.criarCorrelacoes(v, correlacao[v], mapeamentoVariaveis))
			constructos[mapeamentoVariaveis[v][1]].variaveis.append(v_resultado)

		resultado = RelatorioResultado(None, None, None, constructos)	
		return resultado

	def mapearVariaveis(self, formulario):
		mapeamentoVariaveis = []
		qtdVariavies = 0;	

		for i in range(0, len(formulario.constructos)):
			for v in formulario.constructos[i].variaveis:
				mapeamentoVariaveis.append((v.nome, i))
				qtdVariavies += 1
		return mapeamentoVariaveis, qtdVariavies

	def avaliarFormulario(self, formularios):
		mapeamentoVariaveis, qtdVariavies = self.mapearVariaveis(formularios[0])
		resultado = np.empty(shape=(0,qtdVariavies))		## matriz com as medias das variaveis para cada form
		variaveisForm = np.empty(shape=(0,qtdVariavies)) 	## matriz com das variaveis para cada form. Utilizado para calcular o alfa

		for f in formularios:
			variaveisMedias = []
			for c in f.constructos:
				variaveis = []
				for v in c.variaveis:
					respostas = []
					variaveis.append(v)
					for q in v.questoes:
						respostas.append(q.resposta)
					mediaVariavel = np.mean(np.array(respostas))
					variaveisMedias.append(mediaVariavel)
			resultado = np.vstack([resultado, variaveisMedias])
			variaveisForm = np.vstack([variaveisForm, variaveis])
		
		constructos = formularios[0].constructos

		alfas = self.calcularAlfaVariavies(variaveisForm)

		resultado = self.avaliarVariaveis(resultado, mapeamentoVariaveis, constructos, alfas)
		resultado.nome = nome = formularios[0].nome
		print ("Resultado")
		print(resultado)
		return resultado

	def gerarRelatorio(self, formularios):
		return self.avaliarFormulario(formularios)
		

	def criarCorrelacoes(self, variavelCorrente, correlacoes, mapeamentoVariaveis):
		correlacoesVariaveis = []
		for i in range(0, len(correlacoes)):
			correlacoesVariaveis.append(CorrelacaoVariaveis("",mapeamentoVariaveis[i][0], correlacoes[i]))

		return correlacoesVariaveis

	def gerarRelatorioTeste(self):
		relatorio = RelatorioResultado(None, None, None, [])
		relatorio.nome = "TWQ - Teste"
		relatorio.dataInicial = "10/10/2017"
		relatorio.dataFinal = "16/10/2017"

		constructo1 = Constructo("TWQ", [])

		correlacoesV1 = [CorrelacaoVariaveis(1, "Comunicacao", 0.0), CorrelacaoVariaveis(2, "Coordenacao", 0.5), CorrelacaoVariaveis(3, "Balanco da contribuicao", 0.5), CorrelacaoVariaveis(4, "Suporte mutuo", 0.5), CorrelacaoVariaveis(5, "Esforco", 0.5), CorrelacaoVariaveis(6, "Coesao", 0.5)]
		correlacoesV2 = [CorrelacaoVariaveis(1, "Comunicacao", 0.5), CorrelacaoVariaveis(2, "Coordenacao", 0.0), CorrelacaoVariaveis(3, "Balanco da contribuicao", 0.5), CorrelacaoVariaveis(4, "Suporte mutuo", 0.5), CorrelacaoVariaveis(5, "Esforco", 0.5), CorrelacaoVariaveis(6, "Coesao", 0.5)]
		correlacoesV3 = [CorrelacaoVariaveis(1, "Comunicacao", 0.5), CorrelacaoVariaveis(2, "Coordenacao", 0.5), CorrelacaoVariaveis(3, "Balanco da contribuicao", 0.0), CorrelacaoVariaveis(4, "Suporte mutuo", 0.5), CorrelacaoVariaveis(5, "Esforco", 0.5), CorrelacaoVariaveis(6, "Coesao", 0.5)]
		correlacoesV4 = [CorrelacaoVariaveis(1, "Comunicacao", 0.5), CorrelacaoVariaveis(2, "Coordenacao", 0.5), CorrelacaoVariaveis(3, "Balanco da contribuicao", 0.5), CorrelacaoVariaveis(4, "Suporte mutuo", 0.0), CorrelacaoVariaveis(5, "Esforco", 0.5), CorrelacaoVariaveis(6, "Coesao", 0.5)]
		correlacoesV5 = [CorrelacaoVariaveis(1, "Comunicacao", 0.5), CorrelacaoVariaveis(2, "Coordenacao", 0.5), CorrelacaoVariaveis(3, "Balanco da contribuicao", 0.5), CorrelacaoVariaveis(4, "Suporte mutuo", 0.5), CorrelacaoVariaveis(5, "Esforco", 0.0), CorrelacaoVariaveis(6, "Coesao", 0.5)]
		correlacoesV6 = [CorrelacaoVariaveis(1, "Comunicacao", 0.5), CorrelacaoVariaveis(2, "Coordenacao", 0.5), CorrelacaoVariaveis(3, "Balanco da contribuicao", 0.5), CorrelacaoVariaveis(4, "Suporte mutuo", 0.5), CorrelacaoVariaveis(5, "Esforco", 0.5), CorrelacaoVariaveis(6, "Coesao", 0.0)]


		variavel1 = VariavelResultado("Comunicacao", 0.73, 3.98, 0.26, correlacoesV1)
		variavel2 = VariavelResultado("Coordenacao", 0.72, 3.78, 0.29, correlacoesV2)
		variavel3 = VariavelResultado("B. contribuicao", 0.58, 3.96, 0.30, correlacoesV3)
		variavel4 = VariavelResultado("Suporte mutuo", 0.85, 4.06, 0.29, correlacoesV4)
		variavel5 = VariavelResultado("Esforco \t", 0.76, 3.98, 0.34, correlacoesV5)
		variavel6 = VariavelResultado("Coesao \t", 0.86, 3.92, 0.28, correlacoesV6)

		constructo1.variaveis = [variavel1, variavel2, variavel3, variavel4, variavel5, variavel6]

		relatorio.constructos.append(constructo1)

		print ("Resultado: ")
		print (relatorio)

		print ("Correlacoes entre as variaveis: ")
		print ("\t\t\t 1 \t 2 \t 3 \t 4 \t 5 \t 6")
		for v in constructo1.variaveis:
			result = ""
			for c in v.correlacoes:
				result += "\t" + c.valor.__str__()
			print (" - ", v.nome, result)

		return relatorio

	def formulariosMockup(self):
		formularios = []
		
		formulario = Formulario("TWQ", "Form mock up TWQ", 1, None)
		constructo1 = Constructo("TWQ", [])
		variavel1 = Variavel("Comunicacao", [Questao("Pergunta 1", False, 4), Questao("Pergunta 2", False, 3)])
		variavel2 = Variavel("Coordenacao", [Questao("Pergunta 1", False, 1), Questao("Pergunta 2", False, 5)])
		constructo1.variaveis = [variavel1, variavel2]
		formulario.constructos = [constructo1]
		
		formularios.append(formulario)

		formulario = Formulario("TWQ", "Form mock up TWQ", 2, None)
		constructo1 = Constructo("TWQ", [])
		variavel1 = Variavel("Comunicacao", [Questao("Pergunta 1", False, 2), Questao("Pergunta 2", False, 2)])
		variavel2 = Variavel("Coordenacao", [Questao("Pergunta 1", False, 3), Questao("Pergunta 2", False, 4)])
		constructo1.variaveis = [variavel1, variavel2]
		formulario.constructos = [constructo1]
		
		formularios.append(formulario)

		formulario = Formulario("TWQ", "Form mock up TWQ", 3, None)
		constructo1 = Constructo("TWQ", [])
		variavel1 = Variavel("Comunicacao", [Questao("Pergunta 1", False, 4), Questao("Pergunta 2", False, 5)])
		variavel2 = Variavel("Coordenacao", [Questao("Pergunta 1", False, 4), Questao("Pergunta 2", False, 4)])
		constructo1.variaveis = [variavel1, variavel2]
		formulario.constructos = [constructo1]
		
		formularios.append(formulario)

		return formularios



#analisador = Analisador()
#formularios = analisador.formulariosMockup()
#analisador.gerarRelatorio(formularios)
#analisador.gerarRelatorioTeste()
