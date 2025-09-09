lista_compras=[]
escolha_menu=1

print("Bem-vindo à sua lista de compras!")

while escolha_menu!=4:
    print("1-Adicionar itens à minha lista")
    print("2-Editar um item da minha lista")
    print("3-Excluir um item da minha lista")
    print("4-Finalizar minha lista")
    escolha_menu=int(input("Escolha a opção desejada: "))  
    
    #Adicionar itens na lista
    if escolha_menu==1:
        n_itens=int(input("Digite quantos itens você deseja colocar na lista de compras: "))
        count=0
        for i in range(n_itens):
            lista_compras.append(input("Digite o item para adicionar à lista de compras: "))
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

lista_formatada=", ".join(lista_compras)
    
print("A sua lista está pronta, você precisa comprar:")
for item in lista_compras:
    print(item)
print("Boas compras!")


