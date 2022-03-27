from arquivo import ler_arquivo



def get_veiculos(nome_veiculo):
    list_dados_veiculo = ler_arquivo(nome_veiculo)

    return list_dados_veiculo


def get_pessoa(nome_pessoa):
    list_dados_pessoa = ler_arquivo(nome_pessoa)

    return list_dados_pessoa

    
