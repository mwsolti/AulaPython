#Funcao de execucao
def print_ola_mondo():
    print("Ola Mundo")

#Funcao de execucao parametrizada
def print_dia(estado_hora):
    if estado_hora == "dia":
        print("Bom Dia")
    elif estado_hora == "tarde":
        print("Boa Tarde")
    elif estado_hora == "noite":
        print("Boa Noite")
    else:
        print("Valor invalido")

#funcao retorno sem parametro
dados = "XYZ"
def funcao_coleta():
    return dados


#funcao retorno parametrizada
def soma_valores(valor1,valor2):
    total = int(valor1) +int(valor2)
    return total

print(soma_valores(2,2))