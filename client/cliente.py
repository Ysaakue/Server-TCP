from tkinter import END, Tk, Menu, Label, Entry, Button, Text, GROOVE, StringVar, Radiobutton
from socket import AF_INET, socket, SOCK_STREAM, gethostname
import pickle
from grafico import geraGraf
 
class minhaApp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)                                                                        #no construtor da nossa classe, apenas chamamo o construtor da classe pai, tkinter.Tk.__init__()).
        self.parent = parent                                                                            #geralmente necessitaremos  de acessar o pai de um objeto. É uma boa técnica  sempre salvar uma referencia ao pai.
        self.initialize()                                                                               #no método initialize criamos a interface
         
         
    def initialize(self):                                                                               #aqui criamos os widgets que serão apresentados na tela
        self.imcs = [0,0,0,0,0,0,0,0,0,0,0,0]                                                           #inicia os valores de imc
        self.alturas = [0,0,0,0,0,0,0,0,0,0,0,0]                                                        #inicia os valores de altura
        self.massas = [0,0,0,0,0,0,0,0,0,0,0,0]                                                         #inicia os valores de massa

        #criação do menu principal
        topo = self.winfo_toplevel()                                                                    #pegamos aqui a referencia à janela principal
        self.menuBar = Menu(topo)                                                                       #Criamos uma barra de menus nesta janlea
         
        mnuOpcoes = Menu(self.menuBar, tearoff=0)                                                       #criamos o menu Opçoes
        mnuOpcoes.add_command(label="Sobre", command=self.processaSobre)                                #ao comando sobre associamos o método que mostra um tutorial
        mnuOpcoes.add_command(label="Sair", command=self.processaSair)                                  #ao comando sair associamos o método que fecha o programa
        self.menuBar.add_cascade(label="Opções", menu=mnuOpcoes)                                        #associamos estes submenus ao menu arquivo

        topo.config(menu=self.menuBar)                                                                  # display the menu

        self.grid()                                                                                     #vamos dispor os demais objetos na tela dentro de uma grade
        
        self.option = StringVar()                                                                       #variavel para guardar o valor do RadioButton
        self.jan = Radiobutton(text="Janeiro", value="0", var=self.option)                              #radioButton para Janeiro  
        self.fev = Radiobutton(text="Fevereiro", value="1", var=self.option)                            #radioButton para Fevereiro
        self.mar = Radiobutton(text="Março", value="2", var=self.option)                                #radioButton para Março    
        self.abr = Radiobutton(text="Abril", value="3", var=self.option)                                #radioButton para Abril    
        self.mai = Radiobutton(text="Maio", value="4", var=self.option)                                 #radioButton para Maio     
        self.jun = Radiobutton(text="Junho", value="5", var=self.option)                                #radioButton para Junho   
        self.jul = Radiobutton(text="Julho", value="6", var=self.option)                                #radioButton para Julho
        self.ago = Radiobutton(text="Agosto", value="7", var=self.option)                               #radioButton para Agosto
        self.set = Radiobutton(text="Setembro", value="8", var=self.option)                             #radioButton para Setembro
        self.out = Radiobutton(text="Outubro", value="9", var=self.option)                              #radioButton para Outubro
        self.nov = Radiobutton(text="Novembro", value="10", var=self.option)                            #radioButton para Novembro
        self.dez = Radiobutton(text="Dezembro", value="11", var=self.option)                            #radioButton para Dezembro
        
        self.jan.grid(row=0, column=0)                                                                  #grid para o radioButton de Janeiro
        self.fev.grid(row=0, column=1)                                                                  #grid para o radioButton de Fevereiro
        self.mar.grid(row=0, column=2)                                                                  #grid para o radioButton de Março
        self.abr.grid(row=0, column=3)                                                                  #grid para o radioButton de Abril
        self.mai.grid(row=0, column=4)                                                                  #grid para o radioButton de Maio
        self.jun.grid(row=0, column=5)                                                                  #grid para o radioButton de Junho
        self.jul.grid(row=1, column=0)                                                                  #grid para o radioButton de Julho
        self.ago.grid(row=1, column=1)                                                                  #grid para o radioButton de Agosto
        self.set.grid(row=1, column=2)                                                                  #grid para o radioButton de Setembro
        self.out.grid(row=1, column=3)                                                                  #grid para o radioButton de Outubro
        self.nov.grid(row=1, column=4)                                                                  #grid para o radioButton de Novembro
        self.dez.grid(row=1, column=5)                                                                  #grid para o radioButton de Dezembro

        self.lblM= Label(self, text="Massa(Kg)")                                                        #este objeto irá apresentar o label de massa
        self.lblM.grid(column=0, row=2, columnspan=2)                                                   #nesta posição
 
        self.lblA= Label(self, text="Altura(cm)")                                                       #este objeto irá apresentar o label de altura
        self.lblA.grid(column=4, row=2, columnspan=2)                                                   #nesta posição
 
        self.entryMassa= Entry(self)                                                                    #criamos o campo de texto onde está disponível o valor de massa
        self.entryMassa.grid(column=0,row=3, columnspan=2,sticky='EW')                                  #deixamos na posição correspondente a primeira coluna, segunda linha
 
        self.entryAltura = Entry(self)                                                                  #criamos o campo de texto onde esta disponivel o valor de altura
        self.entryAltura.grid(column=4,row=3, columnspan=2,sticky='EW')                                 #deixamos na posição correspondente à terceira coluna, segunda linha

        texto =''
        self.lblres= Label(self, text=texto)                                                             #este objeto irá apresentar o resultado
        self.lblres.grid( row=5, columnspan= 5)                                                          #nesta posição

        self.btnCalcula = Button(self,text=u"Calcular IMC",command=self.doCalc)                         #criamos o objeto botão associamos o clicar do botão ao método doCalc
        self.btnCalcula.grid(column=2,row=6)                                                            # e o colocamos na posição coluna 0, linha 3
 
        self.btnGraf = Button(self,text=u"Gerar gráfico",command=self.processaGrafico)                  #criamos o objeto botão associamos o clicar do botão ao método doCalc
        self.btnGraf.grid(column=3,row=6)                                                               # e o colocamos na posição coluna 0, linha 3
 
        self.btnEdit = Button(self,text=u"Editar",command=self.processaEditar)                          #criamos o objeto botão associamos o clicar do botão ao método doCalc
        self.btnEdit.grid(column=5,row=6)

    def doCalc(self):                                                                                   #faz a conexão com o socket e faz as operações
        HOST = gethostname()                                                                            #define o host como local
        PORT = 3333                                                                                     #define a porta
        BUFSIZ = 1024                                                                                   #define o tamanho das mensagens
        ADDR = (HOST, PORT)                                                                             #define o endereço

        serverSocket = socket(AF_INET, SOCK_STREAM)                                                     #define endereço do socket como ipv4 e a conexão TCP
        serverSocket.connect(ADDR)                                                                      #conecta com o endereço definido

        self.lblres.destroy()                                                                            #apaga o label de resposta

        data = {}                                                                                       #cria um dictionary
        data['operacao'] = "1"                                                                          #define operação como 1
        data['massa'] = self.entryMassa.get()                                                           #captura o valor do massa
        data['altura'] = self.entryAltura.get()                                                         #captura o valor da altura
        data['mes'] = self.option.get()

        serverSocket.send(pickle.dumps(data))                                                           #envia os dados
        print("enviado")

        resposta = pickle.loads(serverSocket.recv(BUFSIZ))                                              #revebe os dados
        
        serverSocket.close()                                                                            #termina a conexão

        if resposta['mes'] != -1:                                                                       #se algum mes tiver sido selecioando
            self.imcs[resposta['mes']] = resposta['imc']                                                #salva o imc
            self.alturas[resposta['mes']] = resposta['altura']                                          #salva a altura
            self.massas[resposta['mes']] = resposta['massa']                                            #salva a massa

        texto = "O resultado do seu IMC é {:.2f}, você está {}".format(resposta['imc'],resposta['msg']) #forma o texto que vai ser mostrada ao cliente
        self.lblres= Label(self, text=texto)                                                             #este objeto irá apresentar o resultado
        self.lblres.grid( row=5, columnspan= 5)                                                          #nesta posição

    def processaSobre(self):                                                                            #cria uma janela para mostrar mais sobre o programa
        root = Tk()                                                                                     #cria a janela de ajuda
        root.title('Sobre calculo do IMC')                                                              #especificamos o título de nossa aplicação
        root.geometry('520x250')                                                                        #define as dimenssões da janela

        text = Text(root)                                                                               #cria o objeto onde ficará o texto
        text.pack()                                                                                     #vamos dispor os demais objetos na tela dentro de pacote
        text.insert('insert',   'Você deve informar sua massa(em quilogramas), e altura(em centimentros),\n'                             #texto que vai ser exibido
                                'para que possa ser calculado seu Indice de Massa Corpória(IMC).\n\n'
                                'O calculo vai ser feito em um servidor e o resultado será mostrado por\n'
                                'meio da janela inicial.\n\n'
                                'É possivel também gerar um gráfico com a evolução do IMC, altura e massa\n'
                                'ao longo de um ano, você seleciona o mês no checkbox na parte superior da\n'
                                'tela e calcula o IMC, automaticamente os dados serão salvos enquanto sua\n'
                                'sessão durar, e a qualquer momento é possível gerar o gráfico.\n\n'
                                '\nAutores:Isaac Gondim Geraldo & Victor Ramos de Almeida.')
        root.mainloop()                                                                                 #o programa entra no loop de espera de eventos
         
         
    def processaSair(self):                                                                             #fecha a janela
        self.destroy()                                                                                  #se destroi
    
    def processaGrafico(self):                                                                          #cria os gráfico
        geraGraf(self.imcs, self.alturas, self.massas)                                                  #passa os valores como parametro para gerar o gráfico

    def processaEditar(self):                                                                           #recupera os valores salvos
        mes = self.option.get()                                                                         #pega o mes selecionado
        self.entryAltura.delete(0,END)                                                                  #limpa o Entry de altura
        self.entryAltura.insert(0,str(self.alturas[int(mes)]*100))                                      #coloca o valor salvo referente ao mes selecionado
        self.entryMassa.delete(0,END)                                                                   #limpa o Entry de massa
        self.entryMassa.insert(0,str(self.massas[int(mes)]))                                            #coloca o valor salvo referente ao mes selecionado

if __name__ == "__main__":                                                                              #este é ponto onde o programa se inicia se o programa foi chamado a partir do interpretador python, o _name_  automaticamente será "__main__"
    app = minhaApp_tk(None)                                                                             #criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title('Calculo do IMC')                                                                         #especificamos o título de nossa aplicação
    app.mainloop()                                                                                      #o programa entra no loop de espera de eventos