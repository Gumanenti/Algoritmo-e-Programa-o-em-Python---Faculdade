def menuveiculos(pp):
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


def incluirveiculo(p, g):
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



def listartodosveiculos(p):
    i = 0
    for i in range(len(p)):
        print(p[i][0:2])
        

def listarumveiculo(p):
    a = 0
    x = str(input("Digite a Placa"))
    while x != p[a][0]:
        a += 1
    if x == p[a][0]:
        print(p[a])


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
                    break
                elif alt == 2:
                    novo_tipo = str(input("Digite o novo Tipo do Veículo: "))
                    p[a][1] = novo_tipo
                    print(p[a])
                    break
                elif alt == 3:
                    nova_marca = str(input("Digite a nova Marca do Veículo: "))
                    p[a][2] = nova_marca
                    print(p[a])
                    break
                elif alt == 4:
                    novo_modelo = str(input("Digite o novo Nome: "))
                    p[a][3] = novo_modelo
                    print(p[a])
                    break
                elif alt == 5:
                    novo_ano = int(input("Digite o novo Ano do Veículo: "))
                    p[a][4] = novo_ano
                    print(p[a])
                    break
                elif alt == 6:
                    nova_portas = int(input("Digite a nova quantidade de Portas: "))
                    p[a][5] = nova_portas
                    print(p[a])
                    break
                elif alt == 7:
                    novo_combustivel = str(input("Digite o novo Combustível utilizado: "))
                    p[a][6] = novo_combustivel
                    print(p[a])
                    break
                elif alt == 8:
                    nova_cor = str(input("Digite a nova Cor do Carro: "))
                    p[a][7] = nova_cor
                    print(p[a])
                    break
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


def carrosvazio():
    print("-" * 30)
    print("Não existe nenhum mecânico cadastrado")
    print("-" * 30)
    menuveiculos(listaveiculos)
        

##################_Programa_Principal_###################


carros = []
veiculo = []
listamenu = ["Menu Mecânicos", "Menu Veículos"]
listaveiculos = ["Listar Todos Veículos", "Listar um Veículo", "Incluir Novo Veículo", "Alterar Veículo", "Excluir Veículo"]
menuveiculos(listaveiculos)
