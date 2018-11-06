# -*- coding: UTF-8 -*-

def soma(**val):
    print(val)
    total = val["x"] + val["y"]
    return total

if __name__ == "__main__":
    resultado = soma(x=10,y=12)
    print(resultado)
