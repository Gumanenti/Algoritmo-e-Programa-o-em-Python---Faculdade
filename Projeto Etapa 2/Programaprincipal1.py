def tupla():
    dic = {"cpf":"", "nome":""}
    print(dic["cpf"])
    dic["cpf"] = "5555"
    print(dic["cpf"])

    cpf = input("Digite o cpf")
    nome = "gustavo"
    tupla = (cpf, nome)


def cadastrarMecanico():
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
        print(lista)
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

def alterarElemento():
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
        print(lista)
    arquivo.close()

    a = 0
    cpfalterar = input("Digite o CPF do mecanico: ")
    while cpfalterar not in lista[a][0]:
        a += 1
    if cpfalterar in lista[a][0]:
        print("é igual")
        index_linha = a
        print(index_linha)
        cpf = input("Digite cpf: ")
        nome = input("Digite nome: ")
        datanasc = input("Digite datanasc: ")
        sexo = input("Digite sexo: ")
        salario = input("Digite salario: ")
        emails = input("Digite emails: ")
        telefones = input("Digite telefones: ")
        novos_dadosmecanicos = cpf+";"+nome+";"+datanasc+";"+sexo+";"+salario+";"+emails+";"+telefones+"\n" 

        with open("DadosMecanico.txt",'r') as arquivo:
            texto=arquivo.readlines()
            print(texto)
        with open("DadosMecanico.txt", 'w') as arquivo:
            for i in texto:
                if texto.index(i)==index_linha:
                    arquivo.write(novos_dadosmecanicos)
                else:
                    arquivo.write(i)
        

def excluirElemento():
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
        print(lista)
    arquivo.close()

    a = 0
    cpfalterar = input("Digite o CPF do mecanico: ")
    while cpfalterar not in lista[a][0]:
        a += 1
    if cpfalterar in lista[a][0]:
        print("é igual")
        index_linha = a
        print(index_linha)
        novos_dadosmecanicos = ""

        with open("DadosMecanico.txt",'r') as arquivo:
            texto=arquivo.readlines()
            print(texto)
        with open("DadosMecanico.txt", 'w') as arquivo:
            for i in texto:
                if texto.index(i)==index_linha:
                    arquivo.write(novos_dadosmecanicos)
                else:
                    arquivo.write(i)


###################PROGRAMA_PRINCIPAL#########################333

lista = []
listamenu = ["Menu Mecânicos", "Menu Veículos"]
listamecanico = ["Listar Todos", "Listar Elemento Específico", "Incluir Novo Mecânico", "Alterar", "Excluir Mecãnico"]
listaveiculos = ["Listar Todos Veículos", "Listar um Veículo", "Incluir Novo Veículo", "Alterar Veículo", "Excluir Veículo"]

try:
    print("Menu de Opções")
    c = 0
    for item in listamenu:
        print(c+1,"-", listamenu[c])
        c += 1
    while True:
        opc = int(input("Digite a sua opção: "))
        if opc not in range(1,3):
            print("Essa opção não é válida.")
        elif opc == 1:
            menumecanico(listamecanico)
            break
        elif opc == 2:
            print("menuveiculos(listaveiculos)")
            break
except ValueError:
    print("-" * 30)
    print("Erro. Por favor, digite uma opção correta.")
    print("-" * 30)
    menuprincipal(listamenu)


