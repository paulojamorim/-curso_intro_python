# -*- coding: UTF-8 -*-
class Cesto:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get(self):
        return self.items

if __name__ == "__main__":

    c = Cesto()
    c.add("Abacaxi")

    f = c.get()
    print(f)
