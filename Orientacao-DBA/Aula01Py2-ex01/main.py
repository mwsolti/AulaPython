
from back import troco,verifica_troco


dict_produto  = {
    "Bacon": 2.50,
     "Queijo": 5, 
     "Pão" : 3.25
}

total = 0


while True:
    print("Escolha entre estes produtos: \n " + str(dict_produto))
    produto = input("Digite o Nome do PRoduto: \n")

    if produto == "sair":
        break
    else:
        total +=dict_produto[produto]

dinheiro = float(input("O Total deu: "+str(total)+" Digite o Valor dado pelo cliente"))

troco = troco(total,dinheiro)

status = verifica_troco(troco)

print("Este é o Troco: "+str(troco))

print(status)