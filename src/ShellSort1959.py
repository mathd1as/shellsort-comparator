# -*- coding: utf-8 -*-
# Disponível em: https://github.com/TheAlgorithms/Python/blob/master/sorts/shell_sort.py
import math
class ShellSort1959:
    
    def __init__(self, collection):
       self.collection = collection

    def executar(self):
        n = len(self.collection)
        h = (n / 2)
        
        while h > 0:
                for i in range(h, n):
                    c = self.collection[i]
                    j = i
                    while j >= h and c < self.collection[j - h]:
                        self.collection[j] = self.collection[j - h]
                        j = j - h
                        
                        self.collection[j] = c
                print(n)
                h = int(h / 2)
                
        return self.collection