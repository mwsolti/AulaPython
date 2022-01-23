list_numeros = [2,2]

print(list_numeros)

#Adicnar 1 item a lista
numero = int(input("Digite um numero: "))
list_numeros.append(numero)

print(list_numeros)


#limpar Lista Toda
list_numeros.clear()

print(list_numeros)

#Contar quantidade que um valor aparece em uma  lista
list_numeros = [2,2,3,4,5,6]

qt_valor_lista = list_numeros.count(2)

print(qt_valor_lista)

# COntar tamanho da lista
qt_casas = len(list_numeros)
print(qt_casas)

#Somar Valores
list_numeros = [2,2,2]
soma = sum(list_numeros)
print(soma)

#Remove um valor da lista
list_numeros = [1,2,3]
print(list_numeros)
list_numeros.remove(2)
print(list_numeros)


# #Soma
# soma = list_numeros[0] + list_numeros[1]

# print(soma)
