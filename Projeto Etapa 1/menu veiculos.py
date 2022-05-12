def menuveiculos(p, g):
    print("Menu Veículos")
    c = 0
    for item in p:
        print(c+1,"-", p[c])
        c += 1
    while True:
        vei = int(input("Digite a sua opção: "))
        if vei not in range(1,6):
            print("Essa opção não é válida.")
        elif vei == 1:
            print(p[0])
            listartodos(g)
            if g == []:
                galeravazio()
            break
        elif vei == 2:
            print(p[1])
            if g == []:
                galeravazio()
            else:
                listarumelemento(galera)
        elif vei == 3:
            print(p[2])
            incluirmecanico(mecanico, galera)
            break
        elif vei == 4:
            print(p[3])
            break
        elif vei == 5:
            print(p[4])
            break


def listartodos(p):
    i = 0
    for i in range(len(p)):
        print(p[i][0])


def listarumelemento(p):
    a = 0
    x = int(input("Digite um numero"))
    while x != p[a][0]:
        a += 1
    if x == p[a][0]:
        print(p[a])


def incluirmecanico(p, g):
    while True:
        p.clear()
        cpf = int(input("Digite o CPF do mêcanico: "))
        p.append(cpf)

        nome = str(input("Digite o nome do mêcanico: "))
        p.append(nome)

        datanasc = int(input("Digite a data de nascimento do mêcanico: "))
        p.append(datanasc)

        sexo = str(input("Digite o sexo do mêcanico: "))
        p.append(sexo)

        salario = int(input("Digite o salário do mêcanico: "))
        p.append(salario)

        emails = []
        while True:
            emails.append(str(input("Digite um e-mail: ")))
            maisemail = str(input("Quer acrescentar mais um e-mail? [S/N]"))
            if maisemail in "Nn":
                break
        p.append(emails)

        telefones = []
        while True:
            telefones.append(str(input("Digite um telefone: ")))
            maistelefone = str(input("Quer acrescentar mais um telefone? [S/N] "))
            if maistelefone in "Nn":
                break
        p.append(telefones)
        g.append(p.copy())

        x = str(input("Quer adicionar mais um mecânico?"))
        if x in "Nn":
            break




###############


galera = []
listaveiculo = ["Listar Todos os Veículos", "Listar Veículo Específico", "Incluir Novo Veículo", "Alterar Veículo", "Excluir Veículo"]
menuveiculos(listaveiculo, galera)
