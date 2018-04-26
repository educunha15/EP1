# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 19:12:21 2018

@author: tiago
"""

from firebase import firebase   
firebase = firebase.FirebaseApplication("https://ep1-dsoft-b4aab.firebaseio.com/", None)   
LOJAS = firebase.get("", None)  
#import json
#with open("TESTE.json", "r") as file:
    #json_data = file.read().strip()

#if json_data:
    #LOJAS = json.loads(json_data)
#else:
    #LOJAS = {}

while True:   #Cria-se um loop que continuará enquanto for verdade
    #Cria-se um controle das lojas, a partir do qual o usuário selciona o que deseja fazer
    A = int(input('''Controle de lojas -   
                  0 - Sair
                  1 - Gerenciar estoque de uma loja
                  2 - Adicionar loja
                  3 - Remover loja
                  4 - Imprimir todas as lojas
                  Faça sua escolha:  '''))

    if A == 1:   #Caso o usuário digite 1:
        store = input("Nome da loja:  ")  
        store = store.lower()
        if store not in LOJAS:
            print("Loja não encontrada")
            continue
        else:
            STOCK = LOJAS[store]   #Ele poderá acessar as lojas já existentes e alterar o estoque de cada uma

        while True:
            #Cria-se um controle das lojas, a partir do qual o usuário selciona o que deseja fazer
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
            
            if a == 0:  #Se o usuário digitar 0,
                print ('Até mais!')  #O sistema irá fechar essa secção e retornar ao controle de lojas
                #data_x = LOJAS
                #with open("TESTE.json", "w") as file:
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
                        STOCK[b] = {}  #Adiciona o produto ao dicionário STOCK(as lojas que o usuário adicionou na linha 126)
                        while True:
                            c = int(input('Quantidade inicial:  '))
                            f = float(input('Qual o preço unitário?:  '))
                            if c < 0:
                                print ('A quantidade inicial não pode ser negativa')
                            else:
                                STOCK[b]['Quantidade'] = c  #Adciona a chave quantidade e o seu valor
                            if f < 0:
                                print("Preço não pode ser negativo")
                            else:
                                STOCK[b]["Preço"] = f  #Adiciona a chave preço e o seu valor 
                                break
                        break
                    
            elif a == 2:
                d = input('Nome do produto:  ')
                d = d.lower()
                if d in STOCK:  #Caso o produto esteja no dicionário:
                    del STOCK[d]  #Exclui o produto digitado do dicionário
                    print ('Elemento excluido')  #E imprime uma mensagem avisando que o produto foi excluído
                else:
                    print('Elemento não encontrado')  #Ou imprime a mensagem que não havia tal produto no dicionário
                    
            elif a == 3:
                b = input('Nome do produto:  ')
                b = b.lower()
                if b in STOCK:
                    e = int(input('Quantidade:  '))
                    STOCK[b]['Quantidade'] += e  #Altera a o valor da chave quantidade, podendo aumentar ou diminuir o valor
                    print('Novo estoque de {}: {}'.format(b,STOCK[b]['Quantidade']))
                else:
                    print ('Elemento não encontrado')  #Se o produto não existir no dicionário, o programa imprime que ele não existe
                    
            elif a == 4:
                b = input("Qual o nome do produto?:  ")
                b = b.lower()
                if b in STOCK:  #Caso ele exista:
                    g = float(input("Qual o novo preço unitário?:  "))  #O programa pede ao usuário o novo preço unitário do produto
                    STOCK[b]["Preço"] = g  #Ele vai substituir o preço antigo
                    print("Novo preço é de {0}.".format(float(STOCK[b]["Preço"])))  #O programa imprime um aviso, falando qual é o novo preço
                else:
                    print ('Produto não cadastrado.')
                    
            elif a == 5:
                for i in STOCK:
                    print(i,':',STOCK[i]['Quantidade'])  #Ele imprime quais produtos existem no estoque e a quantidade de cada um
                    #Ele imprime a quantidade de cada produto e o valor total de cada um
                    print("Você possui {0} de {1}. O preço total é de {2}.".format(STOCK[i]['Quantidade'], i, STOCK[i]['Quantidade']*STOCK[i]["Preço"]))
                    if i not in STOCK:
                        print('Estoque vazio')
                        
            elif a == 6:
                for i in STOCK:
                    if STOCK[i]['Quantidade'] < 0:
                        print(i,':',STOCK[i]['Quantidade'])  #O programa imprime quais produtos existem e a quantidade de cada um, porém esta será negativa
                    else:
                        print("Estoque negativo vazio")
                        
            elif a == 7:
                e = 0
                for m in STOCK.values():  #Para cada valor em STOCK
                    e += m["Quantidade"]*m["Preço"]   #Soma o valor total de cada produto
                print("Valor Monetário é de {0}".format(e))  #Imprime o valot monetário (total) do estoque (todos os produtos)
            else:
                print("ERRO")
                
    
    elif A == 0:   #Caso o usuário digite 0:
        print("Até mais!")   #O sistema irá encerrar 
        #data_x = LOJAS
        #with open("TESTE.json", "w") as file:
            #file.write(json.dumps(data_x))
        #firebase.patch(LOJAS, LOJAS[store])
        break
    
    elif A == 2:
        store = input("Nome da loja:  ")  #Pede o nome da loja
        store = store.lower()
        if store in LOJAS:
            print("Loja já cadastrada")  #Se ela já existir, o sistema imprime que ela já está cadastrada
        else:
            LOJAS[store] = {}   #Se ela não existir, cria um dicionário dela dentro do dicionário LOJAS
            firebase.patch("", LOJAS[store])
            print("O cadastro da sua loja será efetuado apenas quando algum produto for cadastrado na mesma.")
    
    elif A == 3:
        j = input("Qual o nome da loja?  ")
        j = j.lower()
        if j in LOJAS:
            del LOJAS[j]  #Exclui a loja do dicionário LOJAS, junto com qualquer estoque que estiver dentro dela
            firebase.delete("", j)
            print("Loja excluída")
        else:
            print("Loja não encontrada")
            
    elif A == 4:
        for e in LOJAS:
            print(e)   #Imprime todas as lojas que estão no dicionário LOJAS
    else:
        print("ERRO")

print(LOJAS)