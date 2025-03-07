# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:15:16 2025

@author: sebas
"""
#librerias en python
import Act7_1_numeros
import Act7_3_abstract


print ("Ingrese un numero: ")
n = int(input())
enteros = Act7_1_numeros.Numeros(n)
enteros.print_numeros()


print ("Ingrese un numero racional: ")
q = float(input())
racionales = Act7_1_numeros.racionales(q)
racionales.print_numeros()

print ("Ingrese numeros para la clase abstracta: ")
m = float (input())
racionales = Act7_3_abstract.racionales(m)
#racionales = Act7_3_abstract.racionales()
racionales.print_numeros()


