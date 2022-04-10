from back import contador_nome,cadastro_cpf,cadastro_pessoa,contador_idade,contador_sexo,cria_arquivo,escreve_arquivo,ler_arquivo

cont = 0


while cont <=10:

    nome = input("Digite o Nome da Pessoa: ")
    cpf= input("Digite o CPF: ")
    idade = int(input("Digite a DIdade: "))
    sexo = input("DIgite M - Masculino ou F -Feminino")

    cadastro_cpf(cpf)

    cadastro_pessoa(nome,cpf,idade,sexo)

    cont +=1

contador_idade()
contador_sexo()
contador_nome()




