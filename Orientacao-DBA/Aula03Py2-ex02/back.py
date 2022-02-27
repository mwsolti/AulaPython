def taxaImposto(imposto,custo):
    imposto = (imposto/100)
    taxa_imposto = custo * imposto
    return taxa_imposto


def soma_imposto(imposto,custo):
    total = custo + imposto
    return total
