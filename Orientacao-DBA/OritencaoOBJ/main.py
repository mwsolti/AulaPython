from back import soma_numeros


numero1 = int(input("Digite o Numero 1"))

numero2 = int(input("Digite o numero 2"))

total1 = numero1 + numero2

total2 = soma_numeros(numero1,numero2)

print ("Soma Tradicional: "+str(total1))

print("Soma da Função: "+str(total2))