# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:05:45 2025

@author: sebas
"""
class Numeros:
    def __init__(self,n):
        self.n = n
    def print_numeros(self):
        for number in range (self.n):
            if ((self.n%2)==0):
                print ("El numero es: ",number)
            else:
                print ("El cuadrado del numero es: ", number**2)

class racionales(Numeros):
    def __init__ (self,n):
        super().__init__(n)
        
    def print_numeros(self):
        print ("El numero raacional es: ", self.n)
        print ("El numero en forma de fraccion es: ", self.n.as_integer_ratio()) 

    def print_hello(self):
        return "Hello Sebastián"
