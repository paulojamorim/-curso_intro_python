# -*- coding: UTF-8 -*-

f = open("notas.txt","r")
lines = f.readlines()

for l in lines:
    print(l)

for l in lines:
    sep = l.split(" ")
    nome = sep[0]
    n1 = float(sep[1])
    n2 = float(sep[2])
    n3 = float(sep[3])
    media = (n1 + n2 + n3) / 3
    print(nome, media)

f.close()
