# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:54:43 2018

@author: Stefano Moretti
"""

from firebase import firebase
firebase = firebase.FirebaseApplication("https://ep1-dsoft-b4aab.firebaseio.com/", None)
LOJAS = firebase.get("", None)
#import json
#with open("DADOS.txt", "r") as file:
    #json_data = file.read().strip()

#if json_data:
    #LOJAS = json.loads(json_data)
#else:
    #LOJAS = {}

while True:
    A = int(input('''Controle de lojas -
                  0 - Sair
                  1 - Gerenciar estoque de uma loja
                  2 - Adicionar loja
                  3 - Remover loja
                  4 - Imprimir todas as lojas
                  Faça sua escolha:  '''))

    if A == 1:
        store = input("Nome da loja:  ")
        store = store.lower()
        if store not in LOJAS:
            print("Loja não encontrada")
            continue
        else:
            STOCK = LOJAS[store]

        while True:
            a = int(input('''Controle de estoque-
                          0 - Sair
                          1 - Adicionar item
                          2 - Remover item
                          3 - Alterar item
                          4 - Alterar preço
                          5 - Imprimir estoque
                          6 - Imprimir estoque negativo
                          7 - Valor Monetário (Preço total)
                          Faça sua escolha:  '''))
            
            if a == 0:
                print ('Até mais!')
                #data_x = LOJAS
                #with open("DADOS.txt", "w") as file:
                    #file.write(json.dumps(data_x))
                firebase.patch('', LOJAS)
                break
            
            elif a == 1:
                while True:
                    b = input('Qual o nome do produto?:  ')
                    b = b.lower()
                    if b in STOCK:
                        print ('Produto já está cadastrado')
                        break
                    else: 
                        STOCK[b] = {} 
                        while True:
                            c = int(input('Quantidade inicial:  '))
                            f = float(input('Qual o preço unitário?:  '))
                            if c < 0:
                                print ('A quantidade inicial não pode ser negativa')
                            else:
                                STOCK[b]['Quantidade'] = c
                            if f < 0:
                                print("Preço não pode ser negativo")
                            else:
                                STOCK[b]["Preço"] = f
                                break
                        break
                    
            elif a == 2:
                d = input('Nome do produto:  ')
                d = d.lower()
                if d in STOCK:
                    del STOCK[d]
                    print ('Elemento excluido')
                else:
                    print('Elemento não encontrado')
                    
            elif a == 3:
                b = input('Nome do produto:  ')
                b = b.lower()
                if b in STOCK:
                    e = int(input('Quantidade:  '))
                    STOCK[b]['Quantidade'] += e
                    print('Novo estoque de {}: {}'.format(b,STOCK[b]['Quantidade']))
                else:
                    print ('Elemento não encontrado')
                    
            elif a == 4:
                b = input("Qual o nome do produto?:  ")
                b = b.lower()
                if b in STOCK:
                    g = float(input("Qual o novo preço unitário?:  "))
                    STOCK[b]["Preço"] = g
                    print("Novo preço é de {0}.".format(float(STOCK[b]["Preço"])))
                else:
                    print ('Produto não cadastrado.')
                    
            elif a == 5:
                for i in STOCK:
                    print(i,':',STOCK[i]['Quantidade'])
                    print("Você possui {0} de {1}. O preço total é de {2}.".format(STOCK[i]['Quantidade'], i, STOCK[i]['Quantidade']*STOCK[i]["Preço"]))
                    if i not in STOCK:
                        print('Estoque vazio')
                        
            elif a == 6:
                for i in STOCK:
                    if STOCK[i]['Quantidade'] < 0:
                        print(i,':',STOCK[i]['Quantidade'])
                    else:
                        print("Estoque negativo vazio")
                        
            elif a == 7:
                e = 0
                for m in STOCK.values():
                    e += m["Quantidade"]*m["Preço"] 
                print("Valor Monetário é de {0}".format(e))
            else:
                print("ERRO")
                
    
    elif A == 0:       
        print("Até mais!")
        #data_x = LOJAS
        #with open("DADOS.txt", "w") as file:
            #file.write(json.dumps(data_x))
        #firebase.patch(LOJAS, LOJAS[store])
        break
    
    elif A == 2:
        store = input("Nome da loja:  ")
        store = store.lower()
        if store in LOJAS:
            print("Loja já cadastrada")
        else:
            LOJAS[store] = {}
            firebase.patch("", LOJAS[store])
            print("O cadastro da sua loja será efetuado apenas quando algum produto for cadastrado na mesma.")
    
    elif A == 3:
        j = input("Qual o nome da loja?  ")
        j = j.lower()
        if j in LOJAS:
            del LOJAS[j]
            firebase.delete("", j)
            print("Loja excluída")
        else:
            print("Loja não encontrada")
            
    elif A == 4:
        for e in LOJAS:
            print(e)
    else:
        print("ERRO")

print(LOJAS)