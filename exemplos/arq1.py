# -*- coding: UTF-8 -*-

frutas = ["Abacate","Manga", "Maçã", "Abacaxi", "Caju"]

f = open("frutas.txt","w")

for item in frutas:
    f.write(item + "\n")

f.close()
