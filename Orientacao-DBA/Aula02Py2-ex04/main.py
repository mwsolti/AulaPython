from back import pesquisa_idade_nome,pesquisa_nomes_idade

dict_nome_idade = {}

op = ""

while True:

    nome = input("Digite o Nome da Pessoa: ")
    idade = int(input("Digite a Idade da Pessoa: "))

    dict_nome_idade[nome] = idade
    op = input("Deseja Para de Cadastrar? ")

    if op == "Sim":
        break



op2 = input("Deseja: \n 1 - Pesquisar uma Idade pelo Nome: \m 2 - Pesquisar Nomes por uma Idade")

if op2 == "1":
    nome = input("Digite o Nome da Pesquisa")
    print(pesquisa_idade_nome(dict_nome_idade,nome))

elif op2 == "2":
    idade = int(input("Digite A Idade que quer pesquisar: "))
    print(pesquisa_nomes_idade(dict_nome_idade,idade))





