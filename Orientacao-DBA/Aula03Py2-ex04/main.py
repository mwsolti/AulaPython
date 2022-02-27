from back import cadastra_lista_compras,cria_arquivo,escreve_arquivo,ler_arquivo


nome_lista = input("Digite o Nome da Lisrta de Compras")

cria_arquivo(nome_lista)

list_compras = cadastra_lista_compras()

escreve_arquivo(nome_lista,list_compras)

op = input("Deseja Visualizar a lista de Compras?")

if op == "sim":

    lst_compras = ler_arquivo(nome_lista)

    for item in lst_compras:
        print(item,)
else:

    print("Acabou!")


