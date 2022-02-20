def verifica_anagrama(string1,string2):

    list_string = list(string2)
    pos1 = 0
    Anagrama = True
    cont_anagram = 0

    while pos1 < len(string1) and Anagrama:
        pos2 = 0
        encontrado = False
        while pos2 < len(list_string) and not encontrado:
            if string1[pos1] == list_string[pos2]:
                encontrado = True
                cont_anagram +=1
            else:
                pos2 +=1

        if encontrado:
            list_string[pos2] = None
        else:
            Anagrama = False

        pos1+=1

    return cont_anagram

string1 = input("Digite a palavra 1: ")

string2 = input("Digite a palavra 2: ")

print(verifica_anagrama(string1,string2))
