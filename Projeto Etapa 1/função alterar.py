def alterarumelemento(p):
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
Digite a opção: 
"""))
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
                nova_datanasc = str(input("Digite a nova Data de Nascimento: "))
                p[a][2] = nova_datanasc
                print(lista[a])
                break
            elif alt == 4:
                novo_sexo = str(input("Digite o novo Nome: "))
                p[a][3] = novo_sexo
                print(lista[a])
                break
            elif alt == 5:
                novo_salario = str(input("Digite o novo Salário: "))
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
                novo_telefones = str(input("Digite o novo Telefone: "))
                p[a][6] = novo_telefones
                print(p[a])
                break
            
            


lista = [[1, 2, 3, 4, 5, ["gu.m", "gig.m"], 7], [4, 5, 6]]
alterarumelemento(lista)
