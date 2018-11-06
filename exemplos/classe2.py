# -*- coding: UTF-8 -*-
class Item:
    def __init__(self):
        self.cor = None

class Fruta(Item):
    def __init__(self):
        self.nome = None
        super().__init__()

    def set_fruta(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def get_fruta(self):
        return [self.nome, self.cor]

if __name__ == "__main__":
    c = Fruta()
    c.set_fruta("Maçã", "Vermelha")
    print(c.get_fruta())
