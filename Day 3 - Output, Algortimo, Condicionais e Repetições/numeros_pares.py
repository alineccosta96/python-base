'''
Faça um programa que imprima numeros pares de 1 a 200.
'''

__author__ = 'Aline'
__version__ = 0.1

i = 1

while i <= 200:
    par = i % 2 
    if par == 0:
        print(f"O número {i} é par")
    i=i+1    
