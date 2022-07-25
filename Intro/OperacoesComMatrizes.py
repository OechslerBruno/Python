# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:49:41 2022

@author: Bruno
"""

print('---- Produto de Matrizes ----')

A = [[1,2],
     [3,4]]

B = [[-1, 3],
     [4, 2]]

M = []

linhas = len(A)
colunas1 = len(A[0])
colunas2 = len(B[0])

for i in range(0, linhas):
    auxLinha = []
    for k in range(0, colunas2):
        soma = 0
        for j in range(0, colunas1):
            soma = soma + A[i][j]*B[j][k]
        auxLinha.append(soma)
    M.append(auxLinha)
    
for lin in range(0, len(M)):
    for col in range(0, len(M[0])):
        print('Linha: ', lin, 'Coluna: ', col, 'Valor: ', M[lin][col])
        
print('---- Matriz Tansposta ----')
C = [[1,2,3,4],
     [10,11,12,13]]

maxLin = len(C)
maxCol = len(C[0])

T = []
for i in range(0, maxCol):
    auxLinha = []
    for j in range(0, maxLin):
        auxLinha.append(C[j][i])
    T.append(auxLinha)
    
for item in T:
    print(item)