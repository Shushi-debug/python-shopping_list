lista_compras=[]

print("Bem-vinde à sua lista de compras!")
n_itens=int(input("Digite quantos itens você deseja colocar na lista de compras: "))
count=0

for i in range(n_itens):
    lista_compras.append(input("Digite o item para adicionar à lista de compras: "))
    
lista_formatada=", ".join(lista_compras)

print("A sua lista de compras é:",lista_formatada)
escolha=int(input("\nEstá faltando algo?\n1-Sim\n2-Não"))

while escolha==1:
    lista_compras.append(input("Digite o item a ser adicionado: "))
    lista_formatada=", ".join(lista_compras)
    print("Sua lista atual tem:",lista_formatada)
    escolha=int(input("Deseja adicionar mais um item?\n1-Sim\n2-Não\n"))

lista_formatada=", ".join(lista_compras)
    
print("A sua lista está pronta, você precisa comprar:")
for item in lista_compras:
    print(item)
print("Boas compras!")


