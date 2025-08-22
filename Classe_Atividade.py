class Chocolate:
    def __init__(self, marca,sabor):
        self.marca = marca
        self.sabor = sabor
    def fabricando(self):
        print(f'O chocolate da marca {self.marca} do sabor {self.sabor} esta sendo fabricado')

chocolate1 = Chocolate('Garoto', 'Chocolate Branco')
chocolate2 = Chocolate('KiBom', 'brigadeiro')

chocolate1.fabricando()
chocolate2.fabricando()