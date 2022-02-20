
from back import lista_compras,pesquina_quantidade_nome,pesquisa_nomes_quantidade,lista_produtos_quantidade


op = input("Digite 1 - Para pesquisar a quantidade um produto pelo Nome: \n 2 - Pesquisar os produtos de uma quantidade X: \n 3 - Listas Produtos \n")


dict_compras = lista_compras()

if op == "1":
    nome = input("Digite o nome do Produto>: ")
    print(pesquina_quantidade_nome(dict_compras,nome))
elif op == "2":
    quantidade = int(input("Digite a quantidade de produtos: "))
    print(str(pesquisa_nomes_quantidade(dict_compras,quantidade)))
elif op == "3":
    lista_produtos_quantidade(dict_compras)
