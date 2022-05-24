# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:02:33 2022

@author: Bruno

Operações com vetores
"""
import math

def PrintResult(soma):
    for valor in soma:
        print(valor)

print('----- SOMA -----')
dados1 = [1,2,3,4]
dados2 = [5,6,7,8]

soma = []
quant = len(dados1)

for ind in range(0,quant):
    soma.append(dados1[ind] + dados2[ind])
    
PrintResult(soma)
    
print('----- SOMA ESCALAR -----')
valor = 0.5

soma = []
for ind in range(0,quant):
    soma.append(dados1[ind]+valor)
    
PrintResult(soma)

print('----- MULTIPLICAÇÃO -----')
dadosMultiplicadores = [0.5, 0.3, 0.9, 0.4]

mult = []
for ind in range(0,quant):
    mult.append(dados1[ind] * dadosMultiplicadores[ind])
    
PrintResult(mult)

print('----- MULTIPLICAÇÃO ESCALAR -----')
mult = []
for ind in range(0,quant):
    mult.append(dados1[ind] * valor)
    
PrintResult(mult)

print('----- PRODUTO ESCALAR DE VETORES -----')
dadosMultiplicadores = [0.5, 0.2, 0.3, 0.4]
soma = 0

for ind in range(0, quant):
    soma = soma + dados1[ind] * dadosMultiplicadores[ind]
    
print(soma)

print('----- DISTÂNCIA VETORES -----')
d1 = [1,2,3,4]
d2 = [2,3,4,5]

soma = 0
quant = len(d1)

for ind in range(0, quant):
    soma = soma + math.pow(d1[ind]-d2[ind], 2)
    
distancia = math.sqrt(soma)
print(distancia)
    
    
    
    
    
    