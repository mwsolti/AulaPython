
from .arquivos import escreve_arquivo,ler_arquivo,cria_arquivo

def cadastro_nome_lista(nome_lista):
    list_nome = [nome_lista]
    escreve_arquivo("cadastro_nome_listas",list_nome)


def ler_nome_lista():
    list_nomes = ler_arquivo("cadastro_nome_listas")
    return list_nomes

def cria_lista(nome_lista):
    cria_arquivo(nome_lista)

def insere_lista(nome_lista,list_itens):
    escreve_arquivo(nome_lista,list_itens)


def ler_lista_compras(nome_lista):
    list_compras = ler_arquivo(nome_lista)
    return list_compras
