from controller.cadastros import cadastro_nome_lista,insere_lista,ler_lista_compras,ler_nome_lista,cria_lista

#Variavel para selecionar opção
opcao = ""


while True:

    opcao = input("Quer Cadastrar Uma Nova Lista? \n 1 - Sim \n 2 - Não \n 3 - Sair: \n")

    if opcao == "1":
        nome_lista = input("Digite o Nome da LIsta: ")
        cadastro_nome_lista(nome_lista)
        cria_lista(nome_lista)

        opcao = input("Digite: \n 1 - Inserir Itens na Lista ou Qualquer coisa para COntinuar")

        if opcao == "1":
            list_compras = []
            while True:
                item = input("Digite o Nome do Produto para inserir na lista ou Sair para FInalisar: ")
                
                if item == "Sair":
                    break
                else:    
                    list_compras.append(item)

            insere_lista(nome_lista,list_compras)
        
        else: 
            opcao = ""
    
    if opcao == "2":

        print("Abaixo Listas ja cadastradas \n")
        
        list_nomes_listas = ler_nome_lista()

        for nome_listas in list_nomes_listas:
            print(nome_listas+"\n")
        

        nome_lista  = input("Digite o nome da lista que deseja Visualisar: ")

        #if nome_lista in list_nomes_listas:
        list_compras = ler_lista_compras(nome_lista)

        for item in list_compras:
            print(item + "\n")
        
        break

    
    if opcao == "3":
        print("VOcÊ Saiu!")
        break

                





