# Class -> Palavra chave em python para definir uma classe
# Carro -> Nome que damos á classe. Por convenção começa com letra maiúscula se for nome composto, usamos Camel Case. Ex:Minha Casa
# Def -> Palavra chave que define uma função ou método no Python
# __init__ -> Método contrutor da classe. Ele é chamado automaticamente quando criamos a classe com um novo bojeto. Serve para inicializar atributos do objeto
# self -> Uma referência ao próprio objeto que está sendo criado
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def acelerar(self):
        print(f'O carro {self.marca}  {self.modelo} está acelerado')

# Criando dois objetos diferentes
carro1 = Carro('Toyota', 'Corola')
carro2 = Carro('Honda', 'Civic')
carro3 = Carro('Subaru', 'Crosstrek')

# Chamando métodos
carro1.acelerar() # Usa os atributos do carro1
carro2.acelerar() # Usa os atributos do carro2
carro3.acelerar() # Usa os atributos do carro