
from .arquivos import cria_arquivo,escreve_arquivo,ler_arquivo

def cadastra_nomes(nome):
    list_nome = [nome]
    escreve_arquivo("cadastro_pessoa",list_nome)


def cria_cadastro_pessoa(nome):
    cria_arquivo(nome)


def popula_cadastro(nome,idade,telefone,email):
    list_dados = [nome,idade,telefone,email]
    escreve_arquivo(nome,list_dados)