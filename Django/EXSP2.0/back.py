from arquivos import cria_arquivo,escreve_arquivo,ler_arquivo

def cadastro_pessoa(nome,sobrenome,cpf,idade,sexo):
    list_pessoa =[]

    cria_arquivo(cpf)

    list_pessoa.append(nome)
    list_pessoa.append(sobrenome)
    list_pessoa.append(cpf)
    list_pessoa.append(idade)
    list_pessoa.append(sexo)

    escreve_arquivo(cpf,list_pessoa)


def cadastro_cpf(cpf):
    list_cpf = [cpf]
    escreve_arquivo("CPFS.txt",list_cpf)


def contador_sexo():
    list_cfs = ler_arquivo("CPFS.txt")

    contM = 0
    contF= 0

    for cpf in list_cfs:
        lisr_dados = ler_arquivo(cpf)

        print (lisr_dados[4])
        
        if lisr_dados[4] == "M":
            contM +=1
        elif lisr_dados[4] =="F":
            contF+=1


    print ("Quantidade Masculinos: "+str(contM))
    print("Quantidade de Femininos: "+str(contF))


def contador_idade():
    list_cfs = ler_arquivo("CPFS.txt")

    contA18 = 0
    contM18 = 0
    contM50 = 0

    for cpf in list_cfs:
        lisr_dados = ler_arquivo(cpf)

        if int(lisr_dados[3]) >= 50:
            contM50 +=1
        elif int(lisr_dados[3]) >=18:
            contM18 +=1
        else:
            contA18 +=1

    print("Quabtidade Menor de 18: "+str(contA18))
    print("Quabtidade Maior de 18: "+str(contM18))
    print("Quabtidade Maior de 50: "+str(contM50))



def contador_nome():
    list_cfs = ler_arquivo("CPFS.txt")
    list_nomes = []

    list_aux =[]
    
    for cpf in list_cfs:
        lisr_dados = ler_arquivo(cpf)
        list_nomes.append(lisr_dados[0])
  
    for nome in list_nomes:
        list_aux.append(nome)
        if nome not in list_aux:
            print("O nome "+nome+" possui: "+list_nomes.count(nome)+" de vezes repetidas")


def contador_sobrenome():
    list_cfs = ler_arquivo("CPFS.txt")
    list_sobrenomes = []

    list_aux =[]
    
    for cpf in list_cfs:
        lisr_dados = ler_arquivo(cpf)
        list_sobrenomes.append(lisr_dados[1])
  
    for sobrenome in list_sobrenomes:
        list_aux.append(sobrenome)
        if sobrenome not in list_aux:
            print("O nome "+sobrenome+" possui: "+list_sobrenomes.count(sobrenome)+" de vezes repetidas")


    
        



        







