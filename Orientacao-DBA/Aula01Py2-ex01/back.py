
def troco(valor_total, dinheiro):
    troco = dinheiro - valor_total
    return troco

def verifica_troco(troco):

    if troco < 0:
        return "Esta faltando dinheiro!"
    else:
        return "Está ai seu Troco!"
