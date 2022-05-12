def tupla():
    dic = {"cpf":"", "nome":""}
    print(dic["cpf"])
    dic["cpf"] = "5555"
    print(dic["cpf"])

    cpf = input("Digite o cpf")
    nome = "gustavo"
    tupla = (cpf, nome)
    print(tupla)

def cadastrarMecanico():
    mecanico = []
    cpf = input("Digite cpf: ")
    mecanico.append(cpf)
    nome = input("Digite nome: ")
    mecanico.append(nome)
    datanasc = input("Digite datanasc: ")
    mecanico.append(datanasc)
    sexo = input("Digite sexo: ")
    mecanico.append(sexo)
    salario = input("Digite salario: ")
    mecanico.append(salario)
    emails = input("Digite emails: ")
    mecanico.append(emails)
    telefones = input("Digite telefones: ")
    mecanico.append(telefones)

    arquivo = open("DadosMecanico.txt", "a")
    dadosmecanico = cpf+";"+nome+";"+datanasc+";"+sexo+";"+salario+";"+emails+";"+telefones+"\n" 
    arquivo.write(dadosmecanico)
    arquivo.close

    tupla = (cpf)
    print(tupla)


def listarTodos():
    print("-" * 30)
    arquivo = open("DadosMecanico.txt", "r")
    c = 0
    lista = []
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        lista.append(dadosaluno)
        print(lista[c])
        c += 1
listarTodos()

def listarUmElemento():
    print("-" * 30)
    arquivo = open("DadosMecanico.txt", "r")
    lista = []
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        lista.append(dadosaluno)
    print(lista)
    print(lista[0][0])
    x = int(input("Digite o cpf: "))
    a = 0
    while x != int(lista[a][0]):
        print("é diferente")
        a += 1
    if x == int(lista[a][0]):
        print(lista[a])

def alterarUmElemento():
    print("-" * 30)
    arquivo = open("DadosMecanico.txt", "r")
    lista = []
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        lista.append(dadosaluno)
    arquivo.close()
    print(lista)
            
##########_PROGRAMA_PRINCIPAL_###########


