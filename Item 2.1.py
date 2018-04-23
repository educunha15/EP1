# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 07:36:37 2018

@author: Stefano Moretti
"""

import json
file = open("DADOS.txt", "r")
json_data = file.read()
file.close()

data_x = json.loads(json_data)

ESTOQUE = data_x

while True:
    a = int(input('''Controle de estoque-
      0 - Sair
      1 - Adicionar item
      2 - Remover item
      3 - Alterar item
      4 - Imprimir estoque
      Faça sua escolha:  '''))
    if a == 0:
        print ('Até mais!')
        data_x = ESTOQUE
        file = open("DADOS.txt", "w")
        file.write(json.dumps(data_x))
        file.close()
        break
    elif a == 1:
        while True:
            b = input('Qual o nome do produto?:  ')
            if b in ESTOQUE:
                print ('Produto já está cadastrado')
                break
            else: 
                ESTOQUE[b] = {}
            while True:
                c = int(input('Quantidade inicial:  '))
                if c < 0:
                    print ('A quantidade inicial não pode ser negativa')
                else:
                    ESTOQUE[b]['Quantidade'] = c
                    break
            break
    elif a == 2:
        d = input('Nome do produto:  ')
        if d in ESTOQUE:
            del ESTOQUE[d]
            print ('Elemento excluido')
        else:
            print('Elemento não encontrado')
    elif a == 3:
        b = input('Nome do produto:  ')
        if b in ESTOQUE:
            e = int(input('Quantidade:  '))
            ESTOQUE[b]['Quantidade'] += e
            print('Novo estoque de {}: {}'.format(b,ESTOQUE[b]['Quantidade']))
        else:
            print ('Elemento não encontrado')
    elif a == 4:
        for i in ESTOQUE:
            print(i,':',ESTOQUE[i]['Quantidade']) 
