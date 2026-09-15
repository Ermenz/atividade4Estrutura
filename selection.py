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
def ordenaSelecao(self):
    for i in range(self.number - 1): 
        min = i
        for j in range(i + 1, self.number):
            j = i + 1
        if self.vet(i) < self.number[min]:
            min = j
    self.vet[min].sef.vet[i]
    self.vet[i].self.vet[min]

    return self

 
def ordenaInsercao(self):    
    for i in range(self.number - 1): 
     now = i
     j = self.number - 1
     while(j > 0 and self.number > now):
      self.vet(j + 1) = self.vet(j)
     

    return  


def bubblesort(self):    
    for i in range(self.number - 1): 
     now = i
     j = self.number - 1
     while(j > 0 and self.number > now):
      self.vet(j + 1) = self.vet(j)
      j = j-1

    return  
        




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