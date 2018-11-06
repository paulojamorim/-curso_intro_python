# -*- coding: UTF-8 -*-
class Item:
    def __init__(self):
        self.__cor = None

    def __teste(self):
        print("aaa")

class Fruta(Item):
    def __init__(self):
        self.nome = None
        super().__init__()

    def set_fruta(self, nome, cor):
        self.nome = nome
        #self.cor = cor

    def get_fruta(self):
        self.__teste()
        return [self.nome, self.cor]

if __name__ == "__main__":

    
    c = Fruta()
    #print(dir(c))
    c.cor = "Azul"
    print(c.cor)
    #c.set_fruta("Maçã", "Vermelha")
    #c.teste()
    #c.get_fruta()
