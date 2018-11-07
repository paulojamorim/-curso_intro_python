# -*- coding: UTF-8 -*-

f = open("frutas.txt","r")
lines = f.readlines()

for l in lines:
    print(l)

f.close()
