# -*- coding: UTF-8 -*-

frutas = ["Abacate","Manga", "Maçã", "Abacaxi", "Caju"]

try:
    print(frutas[10])
except(IndexError):
    print("Erro")
