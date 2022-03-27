from random import random
from arquivo import cria_arquivo
from post import cadastra_veiculos,cadastra_pessoas
from get import get_veiculos,get_pessoa

def cadastra_veiculo(nome_veiculo, marca_modelo,placa,id_usuario= 0):
    cria_arquivo(nome_veiculo)
    cadastra_veiculos(nome_veiculo, marca_modelo,placa,id_usuario)



def busca_veiculo(nome_veiculo):
    list_dados = get_veiculos(nome_veiculo)
    return list_dados


def cadastra_pessoa(nome_pessoa,id):
    cria_arquivo(nome_pessoa)
    cadastra_pessoas(nome_pessoa,id)

def busca_pessoa(nome_pessoa):
    list_dados = get_pessoa(nome_pessoa)
    return list_dados



print(" 1 - Cadastrar Pessoa/Veiculo \n 2 - Buscar Pessoa ou Veiculo")
#print("Digite \n 1 - Para Cadastrar um Veiculo \n 2 - Para Buscar um Veiculo")
opcao = int(input(""))

if opcao == 1:

    nome_pessoa = input("Digite o Nome da Pessoa: ")
    
    id = int(input("Digite o ID!"))

    cadastra_pessoa(nome_pessoa,id)

    print("Pessoa Cadastrada! \n")

    nome_veiculo = input("Digite o Nome Desejado Para o Veiculo: ")
    marca_modelo = input("Digite a Marca\Modelo do Carro: ")
    placa = input("Diite a Placa do Carro:> ")
    id_usuario = id

    cadastra_veiculo(nome_veiculo,marca_modelo,placa,id)

elif opcao == 2:

    print("1 - Pesquisar Pessoa \n 2 - Pesquisar Veiculo")

    opcao = int(input(""))

    if opcao == 1:
        nome_pessoa = input("Digite o Nome da pessoa que quer buscar")
        list_dados = busca_pessoa(nome_pessoa)

    elif opcao == 2:

        nome_veiculo = input("Digite o nome do veiuclo para trazer os dados do mesmo: ")
        list_dados = busca_veiculo(nome_veiculo)

    for dados in list_dados :
        print(dados)




















