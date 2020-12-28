# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:41:20 2020

@author: Bruno
"""

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))


entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

#Classes
saidas = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])

pesos1 = np.array([[-0.017], [-0.893], [0.148]])

#Qtd de rodadas para atualização dos pesos - tempo de treinamento
epocas = 100

for j in range(epocas):
    camadaEntrada = entradas
    #Sinapse são os pesos
    somaSinapse0 = np.dot(camadaEntrada, pesos0) #Etapa do somatório (r = ∑ xi * wi)
    
    camadaOculta = sigmoid(somaSinapse0) #aplicar resultado do somatório na função de ativação