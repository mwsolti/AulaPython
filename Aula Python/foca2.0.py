palavra = "Abacate"

palavra = palavra.lower()

qt_erros = 0
qt_acertos = 0

tamanho_palavra = len(palavra)

list_letras_digitadas = []

print(tamanho_palavra)

game_over = False

while game_over == False:

    letra = input("Digite uma letrra: ")


    if letra in list_letras_digitadas:
        qt_erros +=1
        print("Você ja digitou esta letra: ")
    
    else: 
        list_letras_digitadas.append(letra)

        qt_letras_palavra = palavra.count(letra)
        tamanho_letra_digitada =  len(letra)


        if tamanho_letra_digitada >= tamanho_palavra:

            if letra == palavra:
                print("Você Ganhou o jogo chutando")
                game_over = True
            else:
                print("Perdeu!!!")
                game_over=True

        print (qt_letras_palavra)

        if qt_letras_palavra >=1:
            print("Você Acertou")
            qt_acertos +=qt_letras_palavra
            print(qt_acertos)
        
        else:
            qt_erros += 1
            print("VocÊ Errou! ")

    if qt_erros == 6:
        print("Você Perdeu o jogo")
        game_over = True
    
    if qt_acertos >=  tamanho_palavra:
        print("Você Ganhou o Jogo")
        game_over =True




