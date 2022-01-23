#loops de repetção 

#op = input("Digite [ 1 ] - Par Sair ou Qualquer outra tecla para Continuar a cadastrar: ")
list_aluno = []
list_media = []
cont = 0
while cont != 3:
    cont += 1
    list_aluno.append(input("Digite o Nome do Aluno: "))
    list_media.append(float(input("Digite a Média do ALuno: ")))
    #op = input("Digite 1 - Par Sair ou Qualquer outra tecla para Continuar a cadastrar")
    print(list_aluno)
    print(list_media)



