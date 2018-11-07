# -*- coding: UTF-8 -*-

f = open("notas.txt","r")
lines = f.readlines()

for l in lines:
    items = l.split(' ')
    nome = items[0]
    n1 = float(items[1])
    n2 = float(items[2])
    n3 = float(items[3])
    m = (n1+n2+n3) / 3
    print(nome, m)

f.close()
