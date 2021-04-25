import random
from functions.inputs import *


def numeroAleatorio():
    return random.randint(1, 100)


def distanciaObjetivo(numero, objetivo):
    if numero < objetivo:
        print("Busca un número más grande")
    else:
        print("Busca un número más pequeño")


def game(numero):
    objetivo = numeroAleatorio()

    while numero != objetivo:
        distanciaObjetivo(numero, objetivo)
        numero = get_input(
            int, "Elige un número del 1 al 100: ", "un número valido")
        if numero == objetivo:
            print("¡Ganaste!")


def run():
    numero = get_input(
        int, "Elige un número del 1 al 100: ", "un número valido")
    game(numero)


if __name__ == '__main__':
    run()
