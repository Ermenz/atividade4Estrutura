# Programa principal 
# Avalia o desempenho dos algoritmos de Ordenação
# Calculando o numero de comparações teórico (Complexidade)
# Com o numero de comparações efetivamente realizados pelos algoritmos

import cVetor

import sys
import random
import math
from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
def avaliaOrdenacao(vet, numTestes, funcOrdena):
    numComp     = 0
    mediaComp   = 0
    maxComp     = 0
    minComp     = 10*vet.getTam()*vet.getTam()

    for i in range(numTestes):

        vet.preencheAleatorio()

        print(vet.vetColorRange(0, vet.getTam(), cVetor.bcolors.CRED))

        numComp = funcOrdena()

        print(vet.vetColorRange(0, vet.getTam(), cVetor.bcolors.CGREEN))

        mediaComp += numComp

        if maxComp < numComp:
            maxComp = numComp
        elif minComp > numComp:
            minComp = numComp

    mediaComp /= numTestes

    return minComp, maxComp, mediaComp

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 20

    v = cVetor.cVetor(n)

    minComp, maxComp, mediaComp = avaliaOrdenacao(v, 1, v.ordenaSelecao)

    print("Ordenação por Seleção")
    print("----------------")
    print("valores encontrados:")
    print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    print("valores teóricos:")
    print(f'min - {n*n}     medio - {n*n}     max - {n*n}')
    print("=========================================")

    minComp, maxComp, mediaComp = avaliaOrdenacao(v, 1, v.ordenaInsercao)

    print("Ordenação por Inserção")
    print("----------------")
    print("valores encontrados:")
    print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    print("valores teóricos:")
    print(f'min - {n}     medio - {n*n}     max - {n*n}')
    print("=========================================")

    minComp, maxComp, mediaComp = avaliaOrdenacao(v, 1, v.ordenaBolha)

    print("Ordenação por Bolha")
    print("----------------")
    print("valores encontrados:")
    print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    print("valores teóricos:")
    print(f'min - {n}     medio - {n*n}     max - {n*n}')
    print("=========================================")