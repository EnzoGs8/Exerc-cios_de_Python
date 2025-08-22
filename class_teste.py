class Chocolate:
    def __init__(self, marca, sabor):
        self.marca = marca
        self.sabor = sabor
    def fabricando(self):
        print(f'O chocolate da {self.marca} do {self.sabor} esta sendo fabricado')