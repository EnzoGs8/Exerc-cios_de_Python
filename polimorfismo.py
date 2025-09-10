'''
O que é Polimorfismo?

É quando um mesmo método tem comportamentos diferentes dependendo da classe que usa.

Pensa assim

Todas as classes têm o método apresentar()

Mas cada classe fala de um jeito próprio quando você chama esse método.
'''


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar (self):
        print(f"Olá, eu sou {self.nome}")

class Cliente(Pessoa):
    def apresentar(self): # mesmo nome, mas comportamento diferente
        print(f"Sou cliente {self.nome}, vim comprar algo.")

class Aluno(Pessoa):
    def aprensentar(self): #mesmo nome, mas compórtamento diferente
        print(f"Sou aluno {self.nome}, estou estudando")

# Criando objeto
p = Pessoa("Carlos")
c = Cliente("Maria")
a = Aluno("joão")

# Chamando o MESMO método "apresentar"
p.apresentar()
c.apresentar()
a.apresentar()