# -*- coding: UTF-8 -*-

frutas = ["Abacate","Manga", "Maçã", "Abacaxi", "Caju"]

legumes = ["Batata","Cenoura","Abóbora", "Mandioca"]

cesto = [frutas, legumes]

for c in cesto:
    print(c)

items = frutas + legumes
print(items)

#ou

frutas.extend(legumes)
print(frutas)
