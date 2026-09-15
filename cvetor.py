# Lab 04 - Analise de Algoritmos de Ordenação
# A partir da Classe Vetor

import random
import array

class bcolors:
    CEND        = '\33[0m'
    CBOLD       = '\33[1m'
    CITALIC     = '\33[3m'

    CBLACK      = '\33[30m'
    CRED        = '\33[31m'
    CGREEN      = '\33[32m'
    CYELLOW     = '\33[33m'
    CBLUE       = '\33[34m'
    CMAGENTA    = '\33[35m'
    CCYAN       = '\33[36m'
    CWHITE      = '\33[37m'

# *******************************************************
# ***                                                 ***
# *******************************************************
class cVetor:

# *******************************************************
    def __init__(self, n=20):

        self.numObjs            = 0
        self.ordenado           = False
        self.mostraOrdenacao    = False
        self.numComp            = 0

        if n < 1:
            n = 20

        self.vet        = array.array('i', [0] * n)
        self.numObjs    = n

        self.preencheAleatorio()

# *******************************************************
    def __str__(self):

        outStr = "[  "

        for i in range(self.numObjs-1):
            outStr += f'{self.vet[i]} , '

        outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr

# *******************************************************
    def vetColorRange(self, i, f, cor):

        outStr = "[  "

        for k in range(self.numObjs-1):
            if (k >= i) and k <= f:
                outStr += f'{cor}{self.vet[k]}{bcolors.CEND} , '
            else:
                outStr += f'{self.vet[k]} , '

        if self.numObjs-1 >= i and self.numObjs-1 <= f:
            outStr += f'{cor}{self.vet[self.numObjs-1]}{bcolors.CEND} ]'
        else:
            outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr

# *******************************************************
    def vetColorKeyPair(self, k, p, cor0, cor1):

        outStr = "[  "

        for i in range(self.numObjs-1):
            if i == k:
                outStr += f'{cor0}{self.vet[i]}{bcolors.CEND} , '
            elif i == p:
                outStr += f'{cor1}{self.vet[i]}{bcolors.CEND} , '
            else:
                outStr += f'{self.vet[i]} , '

        if self.numObjs-1 == k:
            outStr += f'{cor0}{self.vet[self.numObjs-1]}{bcolors.CEND} ]'
        elif self.numObjs-1 == p:
            outStr += f'{cor1}{self.vet[self.numObjs-1]}{bcolors.CEND} ]'
        else:
            outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr

# *******************************************************
    def preencheAleatorio(self):

        for i in range(self.numObjs):
            self.vet[i] = random.randint(0, 1000)

# *******************************************************
    def preencheOrdemCrescente(self):

        for i in range(self.numObjs):
            self.vet[i] = i

# *******************************************************
    def preencheOrdemDecrescente(self):

        for i in range(self.numObjs):
            self.vet[i] = self.numObjs - i

# *******************************************************
    def getTam(self):
        return self.numObjs

# *******************************************************
    def setMostraOrdenacao(self):
        self.mostraOrdenacao = True

# *******************************************************
    def getMostraOrdenacao(self):
        return self.mostraOrdenacao

# *******************************************************
    def resetMostraOrdenacao(self):
        self.mostraOrdenacao = False
 
# *******************************************************
   

    def ordenaSelecao(self):
        for i in range(self - 1): 
            min = i
        for j in range(j + 1, self):
            j = i + 1
        if self.vet(i) < self[min]:
            min = j
        self.vet[min].sef.vet[i]
        self.vet[i].self.vet[min]

        return self.numcomp

# *******************************************************
    def ordenaInsercao(self):
        self.numComp = 0
        return self.numComp

# *******************************************************
    def ordenaBolha(self):
        self.numComp = 0
        return self.numComp

    
# *******************************************************
# *******************************************************
# *******************************************************    
if __name__ == '__main__':

    import sys
    import math
    from datetime import datetime

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 20

    v = cVetor(n)
    v.resetMostraOrdenacao() 

    print("=====================================")
    print("Ordenando Vetor com metodo de Selecao")
    print("=====================================")
    v.preencheAleatorio()
    print(str(v))
    numCompSel = v.ordenaSelecao()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por selecao: {numCompSel}')

    v.preencheOrdemCrescente()
    print(str(v))
    numCompSel = v.ordenaSelecao()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por selecao: {numCompSel}')

    v.preencheOrdemDecrescente()
    print(str(v))
    numCompSel = v.ordenaSelecao()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por selecao: {numCompSel}')

    print("=================================+====")
    print("Ordenando Vetor com metodo de Inserção")
    print("==================================+===")
    v.preencheAleatorio()
    print(str(v))
    numCompIns = v.ordenaInsercao()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por insercao: {numCompIns}')

    v.preencheOrdemDecrescente()
    print(str(v))
    numCompIns = v.ordenaInsercao()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por insercao: {numCompIns}')

    v.preencheOrdemCrescente()
    print(str(v))
    numCompIns = v.ordenaInsercao()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por insercao: {numCompIns}')

    print("===================================")
    print("Ordenando Vetor com metodo da Bolha")
    print("===================================")
    v.preencheAleatorio()
    print(str(v))
    numCompBolha = v.ordenaBolha()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por bolha: {numCompBolha}')

    v.preencheOrdemDecrescente()
    print(str(v))
    numCompBolha = v.ordenaBolha()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por bolha: {numCompBolha}')

    v.preencheOrdemCrescente()
    print(str(v))
    numCompBolha = v.ordenaBolha()
    print(str(v))
    print(f'Numero de comparacoes na ordenacao por bolha: {numCompBolha}')