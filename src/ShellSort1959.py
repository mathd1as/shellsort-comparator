# -*- coding: utf-8 -*-
import math
import time

class ShellSort1959:

    def __init__(self, collection):
        self.collection = collection

    def executar(self):
        n = len(self.collection)
        # Começa contar o tempo de execução do algoritmo
        start = time.time()
        h = n // 2
        k = 1

        while h > 0:
            for i in range(h, n):
                c = self.collection[i]
                j = i
                while j >= h and c < self.collection[j - h]:
                    self.collection[j] = self.collection[j - h]
                    j = j - h
                    self.collection[j] = c
            k = k + 1
            h = n // pow(2, k)

        # Pega o tempo apos a execução do algoritmo 
        end = time.time()
        # Calcula o tempo de execução
        executionTime = end - start
        
        return executionTime
