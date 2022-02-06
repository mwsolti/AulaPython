
def calculadora(valor1,valor2,tipo_operação):

    if tipo_operação == "+":
        return valor1+valor2
    elif tipo_operação =="-":
        return valor1-valor2
    elif tipo_operação =="*":
        return valor1*valor2
    elif tipo_operação =="/":
        return valor1/valor2
    else:
        print("Operação invalida")
        return



def insert_dados_calc():
    valor1= float(input("Digite o Valor 1: "))
    tipo_operacao = input("Digite a Operação (+,-,*,/): ")
    valor2 = float(input("Digite o Valor 2: "))

    print("Resultado: \n"+ str(calculadora(valor1,valor2,tipo_operacao)))



insert_dados_calc()