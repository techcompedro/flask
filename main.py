class Carro:
    def __init__(self, marca, cor, n_portas, modelo, ano):
        self.marca = marca
        self.cor = cor
        self.n_portas = n_portas
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.flash = 0
      

    def ligar(self):
        if self.ligado:
            print('o carro ja estar ligado')

        else:
            print('ligando carro...')  
            self.ligado = True
    
    def desligar(self):
        if not self.ligado:
            print('o carro ja esta desligado')
        else:
            print('desligando carro...')  
            self.ligado = False
    
    def acelerar(self):
        if self.ligado:
            self.flash += 10
            print(f'velocidade atual {self.flash}km')
        
        else:
            print('o carro não pode acelerar porque estar desligado')
        



carro = Carro('Marca1', 'Cor1', 4, 'Modelo1', 2020)

carro.ligar()
carro.ligar()
carro.desligar()
carro.desligar()
carro.acelerar()
carro.ligar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()

