def menuprincipal(p):
    try:
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
                menuveiculos(listaveiculos)
                break
    except ValueError:
        print("-" * 30)
        print("Erro. Por favor, digite uma opção correta.")
        print("-" * 30)
        return menuprincipal(p)


def menumecanico(pp):
    try:
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
    except ValueError:
        print("-" * 30)
        print("Erro. Por favor, digite a opção correta.")
        print("-" * 30)
        return menumecanico(pp)


def incluirmecanico(p, g):
    try:
        while True:
            p.clear()
            print("-" * 30)
            print("O programa não irá permitir adicionar um CPF já cadastrado.")
            print("-" * 30)
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
            try:
                if g[0][0] == g[1][0]:
                    print("-" * 30)
                    print("Erro. CPF já cadastrado.")
                    g.remove(g[1])
                    print("-" * 30)
                if g[0][0] != g[1][0]:
                    h = str(input("quer adicionar"))
                    if h in "Nn":
                        return menumecanico(listamecanico)
                    
            except IndexError:
                x = str(input("Quer adicionar mais um mecânico?"))
                if x in "Nn":
                    return menumecanico(listamecanico)
    except ValueError:
        print("Erro. Por favor, digite novamente o CPF do mecânico que deseja Incluir.")
        return incluirmecanico(p, g)
        



def listartodos(p):
    i = 0
    for i in range(len(p)):
        print(p[i][0:2])
        return menumecanico(listamecanico)
        

def listarumelemento(p):
    try:
        a = 0
        x = int(input("Digite o CPF do mecânico que deseja buscar:"))
        while x != p[a][0]:
            a += 1
        if x == p[a][0]:
            print(p[a])
            return menumecanico(listamecanico)
    except ValueError:
        print("Erro. Por favor, digite novamente o CPF.")
        return listarumelemento(p)


def alterarumelemento(p):
    try:
        a = 0
        x = int(input("Digite o CPF do mecânico que deseja alterar: "))
        
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
                    return menumecanico(listamecanico)
                elif alt == 2:
                    novo_nome = str(input("Digite o novo Nome: "))
                    p[a][1] = novo_nome
                    print(p[a])
                    return menumecanico(listamecanico)
                elif alt == 3:
                    nova_datanasc = int(input("Digite a nova Data de Nascimento: "))
                    p[a][2] = nova_datanasc
                    print(p[a])
                    return menumecanico(listamecanico)
                elif alt == 4:
                    novo_sexo = str(input("Digite o novo Nome: "))
                    p[a][3] = novo_sexo
                    print(p[a])
                    return menumecanico(listamecanico)
                elif alt == 5:
                    novo_salario = int(input("Digite o novo Salário: "))
                    p[a][4] = novo_salario
                    print(p[a])
                    return menumecanico(listamecanico)
                elif alt == 6:
                    print(p[a][5])
                    email_alterado = str(input("Qual email você deseja alterar? "))
                    e = 0
                    while email_alterado not in p[a][5][e]:
                            e += 1
                    if email_alterado in p[a][5][e]:
                        p[a][5][e] = str(input("novo email"))
                        print(p[a])
                        return menumecanico(listamecanico)
                elif alt == 7:
                    print(p[a][6])
                    telefone_alterado = str(input("Qual telefone você deseja alterar? "))
                    t = 0
                    while telefone_alterado != p[a][6][t]:
                            t += 1
                    if telefone_alterado == p[a][6][t]:
                        p[a][6][t] = int(input("novo telefone"))
                        print(p[a])
                        return menumecanico(listamecanico)
    except IndexError:
        print("Erro. Digite novamente o CPF")
        return alterarumelemento(p)


def excluirumelemento(p):
    try:
        a = 0
        x = int(input("Digite o CPF do mecânico que deseja excluir: "))
        while x != p[a][0]:
            a += 1
        if x == p[a][0]:
            p.remove(p[a])
            print(p)
            return menumecanico(listamecanico)
    except (IndexError, ValueError):
        print("-" * 30)
        print("Erro. Por favor, digite novamente o CPF.")
        print("-" * 30)
        return excluirumelemento(p)


def galeravazio():
    print("-" * 30)
    print("Não existe nenhum mecânico cadastrado.")
    print("-" * 30)
    menumecanico(listamecanico)


def menuveiculos(pp):
    try:
        print("Menu Veículos")
        c = 0
        for item in pp:
            print(c+1,"-", pp[c])
            c += 1
        while True:
            car = int(input("Digite a sua opção: "))
            if car not in range(1,6):
                print("Essa opção não é válida.")
            elif car == 1:
                print(pp[0])
                listartodosveiculos(carros)
                if carros == []:
                    carrosvazio()
                break
            elif car == 2:
                print(pp[1])
                if carros == []:
                    carrosvazio()
                else:
                    listarumveiculo(carros)
            elif car == 3:
                print(pp[2])
                incluirveiculo(veiculo, carros)
                break
            elif car == 4:
                print(pp[3])
                if carros == []:
                    carrosvazio()
                else:
                    alterarumveiculo(carros)
                break
            elif car == 5:
                print(pp[4])
                if carros == []:
                    carrosvazio()
                else:
                    excluirumveiculo(carros)
                break
    except ValueError:
        print("-" * 30)
        print("Erro. Por favor, digite a opção correta.")
        print("-" * 30)
        return menuveiculos(pp)

def incluirveiculo(p, g):
    try:
        while True:
            p.clear()
            placa = str(input("Digite a Placa do Veículo: "))
            p.append(placa)

            tipo = str(input("Digite o Tipo do Veículo: "))
            p.append(tipo)

            marca = str(input("Digite a Marca do Veículo: "))
            p.append(marca)

            modelo = str(input("Digite o Modelo do Veículo: "))
            p.append(modelo)

            ano = int(input("Digite o Ano do Veículo: "))
            p.append(ano)

            portas = int(input("Digite o Número de Portas: "))
            p.append(portas)

            combustivel = str(input("Digite o Combustível utilizado: "))
            p.append(combustivel)

            cor = str(input("Digite a Cor do Veículo: "))
            p.append(cor)
            g.append(p.copy())

            x = str(input("Quer adicionar mais um mecânico? [S/N] "))
            if x in "Nn":
                return menuveiculos(listaveiculos)
    except ValueError:
        print("-" * 30)
        print("Erro. Por favor, digite novamente a Placa do Veículo.")
        print("-" * 30)
        return incluirveiculo(p, g)



def listartodosveiculos(p):
    i = 0
    for i in range(len(p)):
        print(p[i][0:2])
        return menuveiculos(listaveiculos)
        

def listarumveiculo(p):
    a = 0
    x = str(input("Digite a Placa"))
    while x != p[a][0]:
        a += 1
    if x == p[a][0]:
        print(p[a])
        return menuveiculos(listaveiculos)


def alterarumveiculo(p):
    try:
        a = 0
        x = str(input("Digite a Placa: "))
        
        while x != p[a][0]:
            a += 1
        if x == p[a][0]:
            while True:
                alt = int(input("""Qual opção você deseja alterar?
    1 - Placa
    2 - Tipo
    3 - Marca
    4 - Modelo
    5 - Ano
    6 - Portas
    7 - Combustível
    8 - Cor
    Digite a opção: """))
                if alt not in range(1,8):
                    print("Essa opção não é válida.")
                elif alt == 1:
                    nova_placa = str(input("Digite a nova Placa: "))
                    p[a][0] = nova_placa
                    print(p[a])
                    return menuveiculos(listaveiculos)
                elif alt == 2:
                    novo_tipo = str(input("Digite o novo Tipo do Veículo: "))
                    p[a][1] = novo_tipo
                    print(p[a])
                    return menuveiculos(listaveiculos)
                elif alt == 3:
                    nova_marca = str(input("Digite a nova Marca do Veículo: "))
                    p[a][2] = nova_marca
                    print(p[a])
                    return menuveiculos(listaveiculos)
                elif alt == 4:
                    novo_modelo = str(input("Digite o novo Nome: "))
                    p[a][3] = novo_modelo
                    print(p[a])
                    return menuveiculos(listaveiculos)
                elif alt == 5:
                    novo_ano = int(input("Digite o novo Ano do Veículo: "))
                    p[a][4] = novo_ano
                    print(p[a])
                    return menuveiculos(listaveiculos)
                elif alt == 6:
                    nova_portas = int(input("Digite a nova quantidade de Portas: "))
                    p[a][5] = nova_portas
                    print(p[a])
                    return menuveiculos(listaveiculos)
                elif alt == 7:
                    novo_combustivel = str(input("Digite o novo Combustível utilizado: "))
                    p[a][6] = novo_combustivel
                    print(p[a])
                    return menuveiculos(listaveiculos)
                elif alt == 8:
                    nova_cor = str(input("Digite a nova Cor do Carro: "))
                    p[a][7] = nova_cor
                    print(p[a])
                    return menuveiculos(listaveiculos)
    except IndexError:
        print("Erro. Digite novamente a Placa")
        return alterarumveiculo(p)


def excluirumveiculo(p):
    a = 0
    x = str(input("Digite um numero"))
    while x not in p[a][0]:
        a += 1
    if x in p[a][0]:
        p.remove(p[a])
        print(p)
        return menuveiculos(listaveiculos)


def carrosvazio():
    print("-" * 30)
    print("Não existe nenhum mecânico cadastrado")
    print("-" * 30)
    menuveiculos(listaveiculos)
        

##################_Programa_Principal_###################


galera = []
mecanico = []

carros = []
veiculo = []

listamenu = ["Menu Mecânicos", "Menu Veículos"]
listamecanico = ["Listar Todos", "Listar Elemento Específico", "Incluir Novo Mecânico", "Alterar", "Excluir Mecãnico"]
listaveiculos = ["Listar Todos Veículos", "Listar um Veículo", "Incluir Novo Veículo", "Alterar Veículo", "Excluir Veículo"]
menuprincipal(listamenu)
