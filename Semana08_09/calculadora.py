import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget): # extende os métodos da classe pai para MainWindow
    def __init__(self): 
        super().__init__() # chama init da classe pai
        self.setWindowTitle('Calculadora') #nome da aplicação
        self.setLayout(qtw.QVBoxLayout()) #criando QVBox layout 
        self.keypad() 
        self.temp_nums = [] #o que o usuário está digitando, temporário
        self.fin_nums = [] #termo final da operação
        self.clear = False # variável para validar uma nova operação

        self.show()
    
    def keypad(self):
        container = qtw.QWidget() #recebe todo o método acima
        container.setLayout(qtw.QGridLayout()) # cria QGrid layout 

        #botões
        self.tela = qtw.QLineEdit()
        result = qtw.QPushButton('=', clicked = self.func_result)
        clear = qtw.QPushButton('Clear', clicked = self.clear_calc)
        bt9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        bt8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        bt7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        bt6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        bt5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        bt4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        bt3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        bt2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        bt1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        bt0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        soma = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        subt = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        mult = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        divs = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))

        container.layout().addWidget(self.tela,0,0,1,4) # (r,c, n° rows, n° colms) - pega uma linha e 4 colunas
        container.layout().addWidget(result,1,0,1,2)
        container.layout().addWidget(clear,1,2,1,2)
        container.layout().addWidget(bt7,2,0)
        container.layout().addWidget(bt8,2,1) 
        container.layout().addWidget(bt9,2,2)
        container.layout().addWidget(soma,2,3)  
        container.layout().addWidget(bt4,3,0)
        container.layout().addWidget(bt5,3,1) 
        container.layout().addWidget(bt6,3,2)
        container.layout().addWidget(subt,3,3) 
        container.layout().addWidget(bt1,4,0)
        container.layout().addWidget(bt2,4,1) 
        container.layout().addWidget(bt3,4,2)
        container.layout().addWidget(mult,4,3)
        container.layout().addWidget(bt0,5,0,1,3)
        container.layout().addWidget(divs,5,3)
        self.layout().addWidget(container) #coloca widget na MainWindow
      
    def num_press(self, key_number):
        if self.clear:
            self.temp_nums.clear()
            self.fin_nums.clear()
            self.tela.clear()
            self.clear = False
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums) # recebe a lista em uma string com os elementos sem espaçamento
        if self.fin_nums: # fin_nums só é inicializado quando pressiona um operador
            self.tela.setText(''.join(self.fin_nums) + temp_string) #mostra na tela todos as teclas apertadas pelo usuário
        else:
            self.tela.setText(temp_string)  # mostra na tela o último número que o usuário digitou 

    def func_press(self, operator):
        if self.clear: 
            self.temp_nums.clear()
            self.fin_nums.clear()
            self.tela.clear()
            self.clear = False
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator) # fin_nums guarda os valores digitados pelo usuário até o operador, ao pressionar outro numero volta para a função acima
        self.temp_nums = []
        self.tela.setText(''.join(self.fin_nums)) # mostra na tela o número e a operação digitada pelo usuário
    
    def func_result(self):
        try:
            fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums) # concatena as listas em uma string sem espaçamento
            result_string = eval(fin_string) #eval faz o calculo que está na string
            fin_string += '='
            fin_string += str(result_string) 
            self.tela.setText(fin_string) # mostra na tela a string contentendo a operação e o resultado
        except Exception as x: 
            self.tela.setText(str(x))
        self.clear = True 
    
    def clear_calc(self): # método que limpa a tela
        self.tela.clear()
        self.temp_nums = []
        self.fin_nums = []


app = qtw.QApplication([]) #inicializa o app
MainWindow() 
app.exec_() #executa app

