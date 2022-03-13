from controller.cadstro import cadastra_nomes,cria_cadastro_pessoa,popula_cadastro

# Criar Um sistema de Cadastro de pessa
# 	Ter arquivo que ira salvar o nome
# 	Ter 1 arquivo para cada cadastro(nome_pessoa), onde dentro do mesmo ira ter Idade,Telefone,e-mail

# Extra:
# 	Adionar opção de leitura



opcao = ""


while True:

    opcao = input("Deseja Cadastrar \n 1 - Sim \n 2 - Não \n")

    if opcao == "1":
        nome = input("DIgite o Nome para o cadastro: ")
        idade = input("Digite a Idade para o Cadstro")
        telefone = input("Digite o Telefone para o cadastro: ")
        email = input ("Digite o e-mail para o cadastro")

        cadastra_nomes(nome)
        cria_cadastro_pessoa(nome)
        popula_cadastro(nome,idade,telefone,email)
    
    if opcao == "2":
        break

