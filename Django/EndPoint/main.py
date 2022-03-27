from arquivo import cria_arquivo
from post import cadastra_veiculos
from get import get_veiculos

def cadastra_veiculo(nome_veiculo, marca_modelo,placa,id_usuario= 0):
    cria_arquivo(nome_veiculo)
    cadastra_veiculos(nome_veiculo, marca_modelo,placa,id_usuario)



def busca_veiculo(nome_veiculo):
    list_dados = get_veiculos(nome_veiculo)
    return list_dados




print("Digite \n 1 - Para Cadastrar um Veiculo \n 2 - Para Buscar um Veiculo")
opcao = int(input(""))

if opcao == 1:

    nome_veiculo = input("Digite o Nome Desejado Para o Veiculo: ")
    marca_modelo = input("Digite a Marca\Modelo do Carro: ")
    placa = input("Diite a Placa do Carro:> ")

    cadastra_veiculo(nome_veiculo,marca_modelo,placa)

elif opcao == 2:
    nome_veiculo = input("Digite o nome do veiuclo para trazer os dados do mesmo: ")
    list_dados_veiculo = busca_veiculo(nome_veiculo)

    for dados_veiculo in list_dados_veiculo :
        print(dados_veiculo)


















