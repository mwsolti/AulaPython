from back import soma_imposto,taxaImposto

imposto = int(input('Digite o Valor do imposto'))

custo = float(input("Digite o Custo do Produto"))

taxa_imposto =  taxaImposto(imposto,custo)

valor_total = soma_imposto(taxa_imposto,custo)

print("O Valor dcom o imposto é: "+str(valor_total))



