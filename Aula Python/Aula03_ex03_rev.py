list_vogal = ["a","e","i","o","u"]
letra = input("Digite uma letra: ")
txt = "Não é Vogal"

for vogal in list_vogal:
    if letra == vogal:
        txt = "é uma vogal"

print(txt)
