def menuprincipal(p):
    print("Menu de Opções")
    c = 0
    for item in p:
        print(c+1,"-", p[c])
        c += 1
    while True:
        opc = int(input("Digite a sua opção: "))
        if opc not in range(1,3):
            print("Essa opção não é válida.")
        elif opc == 1:
            menumecanico(listamecanico)
            break
        elif opc == 2:
            print(p[1])
            break


def menumecanico(pp):
    print("Menu Mecânicos")
    c = 0
    for item in pp:
        print(c+1,"-", pp[c])
        c += 1
    while True:
        mec = int(input("Digite a sua opção: "))
        if mec not in range(1,6):
            print("Essa opção não é válida.")
        elif mec == 1:
            print(pp[0])
            listartodos(galera)
            if galera == []:
                galeravazio()
            break
        elif mec == 2:
            print(pp[1])
            if galera == []:
                galeravazio()
            else:
                listarumelemento(galera)
        elif mec == 3:
            print(pp[2])
            incluirmecanico(mecanico, galera)
            break
        elif mec == 4:
            print(pp[3])
            if galera == []:
                galeravazio()
            else:
                alterarumelemento(galera)
            break
        elif mec == 5:
            print(pp[4])
            if galera == []:
                galeravazio()
            else:
                excluirumelemento(galera)
            break


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
            return menumecanico(listamecanico)



def listartodos(p):
    i = 0
    for i in range(len(p)):
        print(p[i][0:2])
        

def listarumelemento(p):
    a = 0
    x = int(input("Digite um numero"))
    while x != p[a][0]:
        a += 1
    if x == p[a][0]:
        print(p[a])


def alterarumelemento(p):
    try:
        a = 0
        x = int(input("Digite um CPF"))
        
        while x != p[a][0]:
            a += 1
        if x == p[a][0]:
            while True:
                alt = int(input("""Qual opção você deseja alterar?
    1 - CPF
    2 - Nome
    3 - Data de Nascimento
    4 - Sexo
    5 - Salário
    6 - E-mails
    7 - Telefones
    Digite a opção: """))
                if alt not in range(1,8):
                    print("Essa opção não é válida.")
                elif alt == 1:
                    novo_cpf = int(input("Digite o novo CPF: "))
                    p[a][0] = novo_cpf
                    print(p[a])
                    break
                elif alt == 2:
                    novo_nome = str(input("Digite o novo Nome: "))
                    p[a][1] = novo_nome
                    print(p[a])
                    break
                elif alt == 3:
                    nova_datanasc = int(input("Digite a nova Data de Nascimento: "))
                    p[a][2] = nova_datanasc
                    print(p[a])
                    break
                elif alt == 4:
                    novo_sexo = str(input("Digite o novo Nome: "))
                    p[a][3] = novo_sexo
                    print(p[a])
                    break
                elif alt == 5:
                    novo_salario = int(input("Digite o novo Salário: "))
                    p[a][4] = novo_salario
                    print(p[a])
                    break
                elif alt == 6:
                    print(p[a][5])
                    email_alterado = str(input("Qual email você deseja alterar? "))
                    e = 0
                    while email_alterado not in p[a][5][e]:
                            e += 1
                    if email_alterado in p[a][5][e]:
                        p[a][5][e] = str(input("novo email"))
                        print(p[a][5])
                        break
                elif alt == 7:
                    print(p[a][6])
                    telefone_alterado = int(input("Qual telefone você deseja alterar? "))
                    t = 0
                    while telefone_alterado != p[a][6][t]:
                            t += 1
                    if telefone_alterado == p[a][6][t]:
                        p[a][6][t] = int(input("novo telefone"))
                        print(p[a][6])
                        break
    except IndexError:
        print("Erro. Digite novamente o CPF")
        return alterarumelemento(p)


def excluirumelemento(p):
    a = 0
    x = int(input("Digite um numero"))
    while x != p[a][0]:
        a += 1
    if x == p[a][0]:
        p.remove(p[a])
        print(p)


def galeravazio():
    print("-" * 30)
    print("Não existe nenhum mecânico cadastrado")
    print("-" * 30)
    menumecanico(listamecanico)
        
########


galera = []
mecanico = []
listamenu = ["Menu Mecânicos", "Menu Veículos"]
listamecanico = ["Listar Todos", "Listar Elemento Específico", "Incluir Novo Mecânico", "Alterar", "Excluir Mecãnico"]
menuprincipal(listamenu)
