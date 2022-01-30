dict_produto = {"queijo":2,"bacon":4,"leite":5}

#Adicionar uma novachave/valor no dicionario usando input(Usuairo coloca valor)


#produto = input("Digite um produto: ")

#valor = float(input("Digite o Valor do Produto: "))

#dict_produto[produto] = valor


print(dict_produto)


#PEgar todas as chaves do dict

chaves = dict_produto.keys()

print(chaves)


#PEgar só valores do dict

valores = dict_produto.values()

print(valores)


#Utilizando funç~eos de dict
soma = 0
for valor in valores:
    soma +=valor

print(soma)