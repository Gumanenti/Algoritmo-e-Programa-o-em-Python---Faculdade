def alterarumelemento(p):
    a = 0
    x = int(input("Digite um numero"))
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
                lista[a][0] = novo_cpf
                print(lista[a])
                break
            elif alt == 2:
                print("deu")
            
            
                
            


lista = [[1, 2, 3], [4, 5, 6]]
alterarumelemento(lista)
