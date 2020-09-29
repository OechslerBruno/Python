# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:40:54 2020

@author: Bruno
@description: Perceptron de uma camada
"""

import numpy as np

entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):    
    return e.dot(p)
    #dot product / produto escalar

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

s = soma(entradas, pesos)
r = stepFunction(soma(entradas, pesos))