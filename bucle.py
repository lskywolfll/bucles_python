from functions.inputs import get_input

def calculo_potencia(base = 2, exponente = 0, limite = 1):
    resultado = 0

    while resultado < limite:
        resultado = base ** exponente
        print(f"{base} elevado a {exponente} es igual a: {resultado}")
        exponente += 1


def run():
    LIMITE = get_input(int, "Numero maximo ?: ", "un numero valido")
    calculo_potencia(limite=LIMITE)


if __name__ == '__main__':
    run()