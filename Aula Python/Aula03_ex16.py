dict_cripto = {}

txt = ""

dict_cripto["0"] = "XXX"
dict_cripto["1"] = "XXY"
dict_cripto["2"] = "XYY"
dict_cripto["3"] = "YYY"
dict_cripto["4"] = "YYZ"
dict_cripto["5"] = "YZZ"
dict_cripto["6"] = "ZZZ"
dict_cripto["7"] = "ZZU"
dict_cripto["8"] = "ZUU"
dict_cripto["9"] = "UUU"

numero = input("Digite UM numero para cripyografar")


for cript in numero:
     txt+=dict_cripto[cript]


if "U" in txt:
    print("Este numero é superior a 7")


print(txt)