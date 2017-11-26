import pandas as pd
import unittest

from entidades.constructo import Constructo
from entidades.variavel import Variavel
from entidades.questao import Questao
from entidades.membro import Membro
from entidades.formulario import Formulario
from Analisador import Analisador 

#pegando o data set completo e pegando subsets
twq_dataset = pd.read_csv('TWQDATA.csv')
twq_subset = twq_dataset[['Membro']]
respostaInvertido = [0,5,4,3,2,1]


#preenche as questoes
def fillQuestions(tipo,idMembro):
 tempQuestoes = []
 if "Comunicacao"==tipo:
  for j in range(2,12):
   pergunta = twq_dataset.iloc[0,j]
   resposta = int(twq_dataset.iloc[idMembro,j]) #id passado
   invertido = "INVERTIDO" in  pergunta
   if invertido:
     resposta = respostaInvertido[resposta]
   questao = Questao(pergunta,invertido,resposta)
   tempQuestoes.append(questao)
 elif "Coordenacao"==tipo :
   for j in range(12,16):
    pergunta = twq_dataset.iloc[0,j]
    resposta = int(twq_dataset.iloc[idMembro,j]) #id passado
    invertido = "INVERTIDO" in  pergunta
    if invertido:
     resposta = respostaInvertido[resposta]
    questao = Questao(pergunta,invertido,resposta)
    tempQuestoes.append(questao)
 elif "Suporte"==tipo:
      for j in range(16,23):
       pergunta = twq_dataset.iloc[0,j]
       resposta = int(twq_dataset.iloc[idMembro,j]) #id passado
       invertido = "INVERTIDO" in  pergunta
       if invertido:
        resposta = respostaInvertido[resposta]
       questao = Questao(pergunta,invertido,resposta)
       tempQuestoes.append(questao)
 elif "Esforco"==tipo:
      for j in range(23,27):
       pergunta = twq_dataset.iloc[0,j]
       resposta = int(twq_dataset.iloc[idMembro,j]) #id passado
       invertido = "INVERTIDO" in  pergunta
       if invertido:
        resposta = respostaInvertido[resposta]
       questao = Questao(pergunta,invertido,resposta)
       tempQuestoes.append(questao)
 elif "Coesao"==tipo:
    for j in range(27,37):
     pergunta = twq_dataset.iloc[0,j]
     resposta = int(twq_dataset.iloc[idMembro,j]) #id passado
     invertido = "INVERTIDO" in  pergunta
     if invertido:
      resposta = respostaInvertido[resposta]
     questao = Questao(pergunta,invertido,resposta)
     tempQuestoes.append(questao)
 elif "Contribuicao"==tipo:
    for j in range(37,40):
     pergunta = twq_dataset.iloc[0,j]
     resposta = int(twq_dataset.iloc[idMembro,j]) #id passado
     invertido = "INVERTIDO" in  pergunta
     if invertido:
      resposta = respostaInvertido[resposta]
     questao = Questao(pergunta,invertido,resposta)
     tempQuestoes.append(questao)
 return tempQuestoes


nomeVariavel = ["Comunicacao","Coordenacao","Suporte","Esforco","Coesao","Contribuicao"]
formularios = []
#Info Formulario
nome = "Relatorio 1"
descricao = "Relatorio 1 TWQ inicial avaliando desempenho do time"



constructoNome = "TWQ"
cargo = "programador"

for x in range(5,14):
 constructos = []
 variavels = []
 constructo = Constructo(constructoNome,variavels)
 for i in range(0,6):
     questoes = []
     questoes = fillQuestions(nomeVariavel[i],x)
     #print(questoes[0].pergunta)
     #print(questoes[0].resposta)
     variavelTemp = Variavel(nomeVariavel[i],questoes)
     constructo.variaveis.append(variavelTemp)

 constructos.append(constructo)
 #print(twq_subset.at[x,'Membro'])
 membro = Membro(twq_subset.at[x,'Membro'],cargo)
 formulario = Formulario(nome,descricao,membro,constructos)
 #print(formulario.membro)
 formularios.append(formulario)



#teste
#print("\n"+formularios[0].nome)
print(formularios[0].constructos[0].variaveis[0].nome)
print(formularios[0].constructos[0].variaveis[0].questoes[4].invertido)
print(formularios[0].membro.nome)
print(formularios[0].membro.cargo)

print(formularios[5].membro.nome)
#print(formularios[3].membro.nome)
#print(len(formularios))




analisador = Analisador()
relatorio = analisador.gerarRelatorio(formularios)


class TestMethods(unittest.TestCase):
    def test_mean(self):
     self.assertEqual(2,4) #Coesão
     self.assertEqual(2,4.19) # 
     self.assertEqual(2,4.57) #
     self.assertEqual(2,3.94) #
     self.assertEqual(2,4.65) #
     self.assertEqual(2,3.83) #
     self.assertEqual(2,4.75) #
     self.assertEqual(2,4.85) #
     self.assertEqual(2,4.55) #
     self.assertEqual(2,4.75) #

    def test_number_questions(self):
     self.assertEqual(len(formularios[0].constructos[0].variaveis[0].questoes),10)
     self.assertEqual(len(formularios[0].constructos[0].variaveis[1].questoes),4)
     self.assertEqual(len(formularios[0].constructos[0].variaveis[2].questoes),7)
     self.assertEqual(len(formularios[0].constructos[0].variaveis[3].questoes),4)
     self.assertEqual(len(formularios[0].constructos[0].variaveis[4].questoes),10)
     self.assertEqual(len(formularios[0].constructos[0].variaveis[5].questoes),3)
   

if __name__ == '__main__':
    unittest.main()





