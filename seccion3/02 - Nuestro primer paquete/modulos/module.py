#!/usr/bin/env python3

""" module.py - Un ejemplo de un módulo en Python """

__contador = 0


def suma(lista):
    global __contador
    __contador += 1
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    return acumulador


def producto(lista):
    global __contador
    __contador += 1
    acumulador = 1
    for elemento in lista:
        acumulador *= elemento
    return acumulador


if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    mi_lista = [i+1 for i in range(5)]
    print(suma(mi_lista) == 15)
    print(producto(mi_lista) == 120)
