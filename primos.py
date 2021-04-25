from functions.inputs import *

def esPrimo(numero):
    contador = 0

    if numero == 1:
        return False

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            print("Entre")
            contador += 1
    
    print(contador)

    if contador == 0:
        return True
    else:
        return False

def run():
    numero = get_input(int, "Escribe un numero: ", "un numero valido")
    if esPrimo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == '__main__':
    run()