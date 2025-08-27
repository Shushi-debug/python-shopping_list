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

lista_formatada=", ".join(lista_compras)
    
print("A sua lista está pronta, você precisa comprar:")
for item in lista_compras:
    print(item)
print("Boas compras!")


