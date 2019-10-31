import matplotlib.pyplot as plt

def geraGraf(imc_mensal, altura_mensal, massa_mensal):                          #função para gerar gráfico
  meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
           'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']    #vetor contendo os meses
  
  plt.rcParams['figure.figsize'] = (14,7)                                       #definindo o tamanho da janela

  plt.subplot(311)                                                              #definido a posição do primeiro grafico
  plt.ylim(0, 60)                                                               #limitando o eixo y do grafico
  plt.title('Gráfico dos dados')                                                #colocando o titulo
  plt.plot(meses,imc_mensal, color='blue')                                      #gera o primeiro grafico em função dos vetoes meses e imc_mensal na cor azul
  plt.ylabel('IMC')                                                             #nomeia o eixo y como IMC

  plt.subplot(312)                                                              #definido a posição do segundo grafico
  plt.ylim(0, 200)                                                              #limitando o eixo y
  plt.plot(meses,massa_mensal, color='red')                                     #gerando o segundo grafico em função dos vetores meses e massa_mensal na cor vermelha
  plt.ylabel('Massa')                                                           #nomeia o eixo y como Massa

  plt.subplot(313)                                                              #definido a posição do ultimo grafico
  plt.ylim(0, 2.50)                                                             #limitando o eixo y
  plt.plot(meses,altura_mensal, color='green')                                  #gerando o ultimo grafico em função dos vetores meses e altura_mensal
  plt.ylabel('Altura')                                                          #nomeia o eixo y como Altura

  plt.show()                                                                    #mostra o grafico gerado

if __name__ == "__main__":                                                      #este é ponto onde o programa se inicia se o programa foi chamado a partir do interpretador python, o _name_  automaticamente será "__main__"
  imc_mensal = [1, 2, 11, 4, 5, 6, 7, 5, 2 ,3, 9, 10]                           #cria valores aleatorios para teste de função
  massa_mensal = [1, 2, 8, 4, 5, 2, 7, 5, 2 ,10, 9, 10] 
  altura_mensal = [1, 15, 3, 3, 5, 6, 7, 2, 2 ,3, 9, 10]
  geraGraf(imc_mensal, altura_mensal, massa_mensal)                             #passa os vetores criados como parametro para o gráfico ser gerado