
from back_robo import ler_arquivo, compara_listas,escreve_diferenca,cria_arquivo


list_compras = ler_arquivo("lista_compras.txt")

list_mercado = ler_arquivo("mercado.txt")

list_diferenca = compara_listas(list_compras,list_mercado)

cria_arquivo("Juriscleudo.txt")

escreve_diferenca("Juriscleudo.txt",list_diferenca)




# for item in list_diferenca:
#     print("Este Item não esta na sua lista: "+str(item))

