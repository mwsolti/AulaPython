from back import contador_nome,cadastro_cpf,cadastro_pessoa,contador_idade,contador_sexo,cria_arquivo,escreve_arquivo,ler_arquivo,contador_sobrenome

cont = 0

cria_arquivo("CPFS.txt")

while cont <=1:

    nome = input("Digite o Nome da Pessoa: ")
    sobrenome = input("Digite o Sobrenom: ")
    cpf= input("Digite o CPF: ")
    idade = int(input("Digite a DIdade: "))
    sexo = input("DIgite M - Masculino ou F -Feminino")

    cadastro_cpf(cpf)

    cadastro_pessoa(nome,sobrenome,cpf,idade,sexo)

    cont +=1

contador_idade()
contador_sexo()
contador_nome()
contador_sobrenome()





