# #Atividade 1

# nota1 = input("Digite a Nota 1: ")
# nota2 = input("Digite a Nota 2  ")
# nota3 = input("Digite a Nota 3  ")

# media = (float(nota1)+float(nota2)+float(nota3))/3

# if media >=7:
#     print ("Você Passou! ")
# elif media >=5:
#     print("Você  está em Recuperação! ")
# else: 
#     print("Você Reprovou")

# print("Sua media é: "+str(media))

#Atividade 2


dia = int(input("Digite o Dia: (de 1 a 30) \n"))

mes = int(input("Digite o M~es (de 1 a 12) \n"))

if dia >=22:
    print("Seu Tipo é: Fantasma")
elif dia >=11:
    print("Seu Tipo é: Eletrico")
else:
    print("Seu Tipo é: Pedra")

if mes >=8:
    print("Seu subtipo é: Planta")
elif mes >=4:
    print("Seu subtipo é: Agua")
else:
    print("Seu subtipo é: Fogo")