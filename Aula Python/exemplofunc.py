#Exemplo Funcoes


from re import S


def caucula_troco(list_valor_item,dinheiro):
    total = 0
    for valor in list_valor_item:
        total +=valor
    
    troco = dinheiro - total

    return troco


def lista_produtos():
    dict_produto = {
        "Bacon": 4,
        "Queijo": 2,
        "Alcatra": 99,
        "Alface": 1,
        "sair": 0

    }

    return dict_produto


def exibe_produtos():
    print("Quais Produtos você Quer? ")
    list_prod= lista_produtos().keys()
    for produto in list_prod:
        print(str(produto) + " - " +" R$ "+ str(float(lista_produtos()[produto])))


def mercadinho():
    produto = ""
    
    list_valores = []
    while produto != "sair":
        exibe_produtos()
        produto = input("Digite o produto quer você deseja: ")
        list_valores.append(lista_produtos()[produto])
    
    dindin = float(input("!Digite o Dinheiro Dado pelo CLiente: "))

    troco = caucula_troco(list_valores,dindin)

    print("Seu troco é: "+str(troco))


mercadinho()