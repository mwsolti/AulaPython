from const import qt_max_pas,qt_pontos_bus

def agrega_passageiro(qt_pas = 0, cont_pontos = 0,total_pass = 0):
    cont_pontos +=1
    qt_pas = int(input("Digite a quantidade de passageiros do ponto "+str(cont_pontos)+": \n"))
    total_pass+= qt_pas
    if total_pass >= qt_max_pas:
        print("Onibus Lootado! ")
        return
    elif cont_pontos >= qt_pontos_bus:
        print("Fium da Linha! ")
        return
    else: 
        agrega_passageiro(qt_pas,cont_pontos,total_pass)






    


