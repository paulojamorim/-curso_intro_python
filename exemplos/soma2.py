# -*- coding: UTF-8 -*-

def soma(*val):
    print(val)
    total = 0
    for v in val:
        total += v
    return total

if __name__ == "__main__":
    resultado = soma(10,5,20)
    print(resultado)
