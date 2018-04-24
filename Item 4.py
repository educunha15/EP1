# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:45:10 2018

@author: tiago
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
      4 - Alterar preço
      5 - Imprimir estoque
      6 - Imprimir estoque negativo
      7 - Valor Monetário
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
                f = float(input('Qual o preço unitário?:  '))
                if c < 0:
                    print ('A quantidade inicial não pode ser negativa')
                else:
                    ESTOQUE[b]['Quantidade'] = c
                if f < 0:
                    print("Preço não pode ser negativo")
                else:
                    ESTOQUE[b]["Preço"] = f
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
        b = input("Qual o nome do produto?:  ")
        if b in ESTOQUE:
            g = float(input("Qual o novo preço unitário?:  "))
            ESTOQUE[b]["Preço"] = g
            print("Novo preço é de {0}.".format(float(ESTOQUE[b]["Preço"])))
        else:
            print ('Produto não cadastrado.')
    elif a == 5:
        for i in ESTOQUE:
            print(i,':',ESTOQUE[i]['Quantidade'])
            print("Você possui {0} de {1}. O preço total é de {2}.".format(ESTOQUE[i]['Quantidade'], i, ESTOQUE[i]['Quantidade']*ESTOQUE[i]["Preço"]))
        if i not in ESTOQUE:
            print('Estoque vazio')
    elif a == 6:
        for i in ESTOQUE:
            if ESTOQUE[i]['Quantidade'] < 0:
                print(i,':',ESTOQUE[i]['Quantidade'])
    elif a == 7:
         e = 0
         for m in ESTOQUE.values():
             e += m["Quantidade"]*m["Preço"] 
         print("Valor Monetário é de {0}".format(e))
        

