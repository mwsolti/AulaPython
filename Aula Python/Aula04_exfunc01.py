
def cadastro(list_nomes):
    dict_cadastro = {}
    codigo = 0
    for nome in list_nomes:
        codigo +=1
        dict_cadastro[codigo] = nome
    
    return dict_cadastro


cont = 0
list_nomes = []

while cont != 3:
    cont +=1
    nome = input("Digite um Nome: ")
    list_nomes.append(nome)


print(cadastro(list_nomes))