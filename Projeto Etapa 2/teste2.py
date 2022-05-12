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
    lista = []
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        lista.append(dadosaluno)
    print(lista)


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
    if x == int(lista[0][0]):
        print("Deu")
    
listarUmElemento()
