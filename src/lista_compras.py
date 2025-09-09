lista_compras=[]
escolha_menu=1

print("\nBem-vindo à sua lista de compras!\n")

while escolha_menu!=5:
    print("\n1-Adicionar itens à minha lista")
    print("2-Editar um item da minha lista")
    print("3-Excluir um item da minha lista")
    print("4-Revisar a minha lista")
    print("5-Finalizar minha lista\n")
    try:
        escolha_menu=int(input("Escolha a opção desejada: "))
    except ValueError:
        print("\nErro! Por favor, digite apenas um número.\n")
        continue
    
    #Adicionar itens na lista
    if escolha_menu==1:        
        while True:
            item_atual=input("Digite um item e dê enter (ou digite 'fim' para terminar):")
            if item_atual=="fim" or item_atual=="Fim":
                break
            else:
                lista_compras.append(item_atual)
                lista_formatada=", ".join(lista_compras)
        print("\nA sua lista de compras atual é:",lista_formatada)
        print(("\nDeseja adicionar mais um item à lista?\n1-Sim\n2-Não, voltar ao menu"))
        try:
            escolha=int(input("\nEscolha a opção desejada: "))
        except ValueError:
            print("\nErro! Por favor, digite apenas um número.")
            continue
        while escolha==1:
            lista_compras.append(input("Digite o item a ser adicionado: \n"))
            lista_formatada=", ".join(lista_compras)
            print("\nItem adicionado com sucesso!\n")
            print("Sua lista atual tem:",lista_formatada)
            print("\nDeseja adicionar mais um item?\n1-Sim\n2-Não")
            try:
                escolha=int(input("\nEscolha a opção desejada: "))
            except ValueError:                
                print("\nErro! Por favor, digite apenas um número.")
                continue
    #Editar itens na lista
    elif escolha_menu==2:
        quer_editar=1
        if len(lista_compras)==0:
            print("\nNão há itens para editar!")
            print("\nVoltando ao menu...\n")
            escolha_menu=1
        elif len(lista_compras)>=1:
            while quer_editar==1:
                print("\nQual item você gostaria de editar?")
                for posicao, item in enumerate(lista_compras):
                    print(posicao+1,item)
                try:
                    escolha_do_usuario=int(input("\nDigite o número do item: "))
                except ValueError:
                    print("\nErro! Por favor, digite apenas um número.")
                    continue
                indice_real=escolha_do_usuario-1
                lista_compras[indice_real]=input("Digite o nome do item para editá-lo: ")
                lista_formatada=", ".join(lista_compras)
                print("\nProduto editado com sucesso!\n")
                print("A sua lista de compras atual é:",lista_formatada)
                print("\nDeseja editar outro item?\n1-Sim\n2-Não, voltar ao menu")
                try:
                    quer_editar=int(input("\nEscolha a opção desejada: "))
                except ValueError:
                    print("\nErro! Por favor, digite apenas um número.")

    #Exclui itens na lista
    elif escolha_menu==3:
        quer_excluir=1
        while quer_excluir==1:
            if len(lista_compras)==0:
                print("\nNão há itens para excluir!\n")
                print("Voltando ao menu...\n")
                escolha_menu=2
            elif len(lista_compras)>=1:
                print("\nQual item você deseja excluir?\n")
                for posicao, item in enumerate(lista_compras):
                    print(posicao+1,item)
                try:
                    escolha_do_usuario=int(input("\nDigite o número do item:"))
                except ValueError:                    
                    print("\nErro! Por favor, digite apenas um número.")
                    continue
                indice_real=escolha_do_usuario-1
                lista_compras.pop(indice_real)
                lista_formatada=", ".join(lista_compras)
                print("\nProduto excluído com sucesso!\n")
                if len(lista_compras)>=1:                    
                    print("A sua lista de compras atual é:",lista_formatada)
                    print("\nDeseja excluir outro item?\n1-Sim\n2-Não, voltar ao menu")
                try:
                    quer_excluir=int(input("\nEscolha a opção desejada: "))
                except ValueError:
                    print("\nErro! Por favor, digite apenas um número.")
                    continue
                else:
                    print("\nA sua lista de compras atual está vazia!")
                    print("Não há mais itens para excluir!")
                    print("\nVoltando ao menu...\n")
                    escolha_menu=2

    #Revisar a lista
    elif escolha_menu==4:
        print("\nA sua lista contém:")
        for posicao, item in enumerate(lista_compras):
                print(item)

lista_formatada=", ".join(lista_compras)
    
print("\nA sua lista está pronta!\n")
for posicao, item in enumerate(lista_compras):
    n_itens=len(lista_compras)
    print(item)
print("Você precisa comprar",n_itens,"itens!")
print("\nBoas compras!\n")


