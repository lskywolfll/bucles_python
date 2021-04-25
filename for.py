from functions.inputs import *

def run():

    frase = get_input(str, "Escribe una frase : ", "un texto valido")
    frase = frase.strip()
    frase = frase.replace(" ","")

    for caracter in frase:
        print(caracter.upper())


if __name__ == "__main__":
    run()
