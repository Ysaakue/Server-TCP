from socket import AF_INET, socket, SOCK_STREAM, gethostname
import pickle 

HOST = gethostname()                                                                            #define o host como local
PORT = 3333                                                                                     #define a porta
BUFSIZ = 1024                                                                                   #define o tamanho das mensagens
ADDR = (HOST, PORT)                                                                             #define o endereço

SERVER = socket(AF_INET, SOCK_STREAM)                                                           #define endereço do socket como ipv4 e a conexão TCP
SERVER.bind(ADDR)                                                                               #vincula o servidor ao endereço

SERVER.listen(10)                                                                               #define o limite de conexões

print("\nservidor socket iniciado!\nEsperando conexão...")

while True:
  clientsocket, client_address = SERVER.accept()                                                #aceita conexão e recebe a referencia para o cliente e o seu endereço
  print("%s:%s foi cenectado." % client_address)

  data = pickle.loads(clientsocket.recv(BUFSIZ))                                                #recebe os dados para fazer o calculo
  
  if data['operacao'] == "1": #IMC
    print("escolheu IMC")
    massa = float(data['massa'])                                                                #atribui massa a uma variavel
    altura = float(data["altura"])                                                              #atribui altura a uma variavel
    try:
      mes = int(data["mes"])                                                                    #atribui mes a uma variavel caso selecionado
    except:
      mes = -1                                                                                  #atribui -1 ao mes caso nenhum mes tenha sido selecioando
    print(mes)

    resultado = {}                                                                              #cria um dictionary
    altura = altura/100                                                                         #converte para metros
    altura = altura * altura                                                                    #calcula potencia de dois
    resultado['imc'] = massa/altura                                                             #calcula o IMC

    if resultado['imc'] < 18.5:
      resultado['msg'] = "abaixo do peso"
    elif resultado['imc'] < 25:
      resultado['msg'] = "no peso normal"
    elif resultado['imc'] < 30:
      resultado['msg'] = "com sobrepeso"
    elif resultado['imc'] < 35:
      resultado['msg'] = "com obesidade de grau 1"
    elif resultado['imc'] < 40:
      resultado['msg'] = "com obesidade de grau 2"
    else:
      resultado['msg'] = "com obesisdade de grau 3"

    if mes != -1:                                                                               #caso algum mes tenha sido selecionado
      resultado['altura'] = float(data["altura"])/100                                           #atribui a altura em centimetro a resposta
      resultado['massa'] = massa                                                                #atribui a massa a resposta
      resultado['mes'] = mes                                                                    #atribui o valor do mes a resposta
    else:
      resultado['mes'] = -1                                                                     #caso nenhum mes tenha sido selecionado define como -1 na resposta

    clientsocket.send(pickle.dumps(resultado))                                                  #envia os resultados

    clientsocket.close()                                                                        #encerra a conexão com o cliente