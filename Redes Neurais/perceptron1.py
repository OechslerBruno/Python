# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:40:54 2020

@author: Bruno
@description: Perceptron de uma camada
"""

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        #print(e[i])
        #print(p[i])
        s += e[i] * p[i]
        
    return s

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

s = soma(entradas, pesos)
r = stepFunction(soma(entradas, pesos))