# -*- coding: UTF-8 -*-

def soma(x, y):
    total = x + y
    return total

if __name__ == "__main__":
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    resultado = soma(a, b)
    print(resultado)
