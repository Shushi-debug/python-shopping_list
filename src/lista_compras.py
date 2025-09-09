lista_compras=[]
escolha_menu=1

print("Bem-vindo à sua lista de compras!")

while escolha_menu!=5:
    print("1-Adicionar itens à minha lista")
    print("2-Editar um item da minha lista")
    print("3-Excluir um item da minha lista")
    print("4-Revisar a minha lista")
    print("5-Finalizar minha lista")
    escolha_menu=int(input("Escolha a opção desejada: "))  
    
    #Adicionar itens na lista
    if escolha_menu==1:        
        while True:
            item_atual=input("Digite um item e dê enter (ou digite 'fim' para terminar):")
            if item_atual=="fim" or item_atual=="Fim":
                break
            else:
                lista_compras.append(item_atual)
                lista_formatada=", ".join(lista_compras)
        print("A sua lista de compras atual é:",lista_formatada)
        print(("\nDeseja adicionar mais um item à lista?\n1-Sim\n2-Não, voltar ao menu"))
        escolha=int(input("Escolha a opção desejada: "))
        while escolha==1:
            lista_compras.append(input("Digite o item a ser adicionado: "))
            lista_formatada=", ".join(lista_compras)
            print("Sua lista atual tem:",lista_formatada)
            print("Deseja adicionar mais um item?\n1-Sim\n2-Não\n")
            escolha=int(input("Escolha a opção desejada: "))
    #Editar itens na lista
    elif escolha_menu==2:
        quer_editar=1
        if len(lista_compras)==0:
            print("Não há itens para editar!")
            print("Voltando ao menu:")
            escolha_menu=1
        elif len(lista_compras)>=1:
            while quer_editar==1:
                print("Qual item você gostaria de editar?")
                for posicao, item in enumerate(lista_compras):
                    print(posicao+1,item)
                escolha_do_usuario=int(input("Digite o número do item: "))
                indice_real=escolha_do_usuario-1
                lista_compras[indice_real]=input("Digite o nome do item para editá-lo: ")
                lista_formatada=", ".join(lista_compras)
                print("Produto editado com sucesso!")
                print("A sua lista de compras atual é:",lista_formatada)
                print("Deseja editar outro item?\n1-Sim\n2-Não, voltar ao menu")
                quer_editar=int(input("Escolha a opção desejada: "))
    #Exclui itens na lista
    elif escolha_menu==3:
        quer_excluir=1
        if len(lista_compras)==0:
            print("Não há itens para excluir!")
            print("Voltando ao menu:")
            escolha_menu=2
        elif len(lista_compras)>=1:
            print("Qual item você deseja excluir?")
            for posicao, item in enumerate(lista_compras):
                print(posicao+1,item)
            escolha_do_usuario=int(input("Digite o número do item:"))
            indice_real=escolha_do_usuario-1
            lista_compras.pop(indice_real)
            lista_formatada=", ".join(lista_compras)
            print("Produto excluído com sucesso!")
            if len(lista_compras)>=1:                    
                print("A sua lista de compras atual é:",lista_formatada)
                print("Deseja excluir outro item?\n1-Sim\n2-Não, voltar ao menu")
                quer_excluir=int(input("Escolha a opção desejada: "))
            else:
                print("A sua lista de compras atual está vazia!")
                print("Não há mais itens para excluir!")
                print("Voltando ao menu...")
                escolha_menu=2
    #Revisar a lista
    elif escolha_menu==4:
        print("A sua lista contém:")
        for posicao, item in enumerate(lista_compras):
                print(item)

lista_formatada=", ".join(lista_compras)
    
print("A sua lista está pronta!")
for posicao, item in enumerate(lista_compras):
    n_itens=len(lista_compras)
    print(item)
print("Você precisa comprar",n_itens,"itens!")
print("Boas compras!")


