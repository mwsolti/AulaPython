
from arquivo import escreve_arquivo

def cadastra_veiculos(nome_veiculo, marca_modelo,placa,id_usuario= 0):
    list_dados_veiculo = [nome_veiculo,marca_modelo,placa,id_usuario]
    escreve_arquivo(nome_veiculo,list_dados_veiculo)


def cadastra_pessoas(nome_pessoa,id):
    list_dados_pessoa = [nome_pessoa,id]
    escreve_arquivo(nome_pessoa,list_dados_pessoa)


