
def run():
    # for contador in range(20):
    #     if contador % 2 != 0:
    #         # Esto provoca que no se imprima el contador
    #         continue
    #     print(contador)

    for i in range(10000):
        print(i)
        if i == 5678:
            # Termina la ejecucion completa del ciclo
            break

if __name__ == '__main__':
    run()