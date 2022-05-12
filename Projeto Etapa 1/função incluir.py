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


def menumecanico(p):
    print("Menu Mecânicos")
    c = 0
    for item in p:
        print(c+1,"-", p[c])
        c += 1
    while True:
        mec = int(input("Digite a sua opção: "))
        if mec not in range(1,6):
            print("Essa opção não é válida.")
        elif mec == 1:
            print(p[0])
            listartodos(galera)
            if galera == []:
                print("-" * 30)
                print("Não existe nenhum mecânico cadastrado")
                menumecanico(listamecanico)
            break
        elif mec == 2:
            print(p[1])
        elif mec == 3:
            print(p[2])
            incluirmecanico(mecanico, galera)
            break
        elif mec == 4:
            print(p[3])
            break
        elif mec == 5:
            print(p[4])
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
            break


def listartodos(p):
    i = 0
    for i in range(len(p)):
        print(p[i][0])
        

def listarumelemento(g):
    y = int(input("Digite o CPF do mecânico: "))
    if y in g:
        elemento = g.index(y)
        print(g)
    else:
        print("Esse mecânico não existe")
        
########


galera = []
mecanico = []
listamenu = ["Menu Mecânicos", "Menu Veículos"]
listamecanico = ["Listar Todos", "Listar Elemento Específico", "Incluir Novo Mecânico", "Alterar", "Excluir Mecãnico"]
menuprincipal(listamenu)
