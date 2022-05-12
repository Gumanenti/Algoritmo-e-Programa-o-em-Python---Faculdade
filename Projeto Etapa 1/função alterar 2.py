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
                    print(lista[a])
                    break
                elif alt == 2:
                    novo_nome = str(input("Digite o novo Nome: "))
                    p[a][1] = novo_nome
                    print(p[a])
                    break
                elif alt == 3:
                    nova_datanasc = int(input("Digite a nova Data de Nascimento: "))
                    p[a][2] = nova_datanasc
                    print(lista[a])
                    break
                elif alt == 4:
                    novo_sexo = str(input("Digite o novo Nome: "))
                    p[a][3] = novo_sexo
                    print(lista[a])
                    break
                elif alt == 5:
                    novo_salario = int(input("Digite o novo Salário: "))
                    p[a][4] = novo_salario
                    print(lista[a])
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

#######


lista = [393771, "gust", 5555, "m", 1500, ["gu.m", "gug.m"], [3333, 44444]], [393777, "gigi", 5555, "f", ["gigi.g", "gig.m"], [5667, 44333]]
alterarumelemento(lista)



