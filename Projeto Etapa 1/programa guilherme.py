def incluirmecanico():
    mecanico = []
    cpf = (input("Digite o CPF do mêcanico: "))
    mecanico.append(cpf)
    if not cpf.isnumeric():
        print('Você não digitou um número. ')
    if cpf.isalpha():
        print('Você digitou uma letra. ')
        
    nome = input("Digite o nome do mêcanico: ")
    mecanico.append(nome)

    datanasc = int(input("Digite a data de nascimento do mêcanico: "))
    mecanico.append(datanasc)

    sexo = input("Digite o sexo do mêcanico: ")
    mecanico.append(sexo)

    salario = int(input("Digite o salário do mêcanico: "))
    mecanico.append(salario)

    emails = []
    while True:
        emails.append(input("Digite um e-mail: "))
        maisemail = str(input("Quer acrescentar mais um e-mail? [S/N]"))
        if maisemail in "Nn":
            break
    mecanico.append(emails)
    
    telefones = []
    while True:
        telefones.append(input("Digite um telefone: "))
        maistelefone = str(input("Quer acrescentar mais um telefone? [S/N] "))
        if maistelefone in "Nn":
            break
    mecanico.append(telefones)

    print(mecanico)

    
############ PROGRAMA PRINCIPAL #################

    
def menuprincipal():
    n = int(input("""[1]Acessar Menu Mecânicos
[2]Acessar Menu Veículos
>>>>> Qual é a sua escolha? """))
    if n == 1:
        print("""[1]Listar Todos mecanicos
[2]Listar só um elemento
[3]Incluir
[4]Alterar
[5]Excluir""")
        mec = int(input(">>>>> Qual é a sua escolha? " ))
        if mec == 3:
            incluirmecanico()

    if n == 2:
        print("""[1]Listar Todos veiculos
[2]Listar só um elemento
[3]Incluir
[4]Alterar
[5]Excluir""")
    else:
        print("Opção Inválida")
        
menuprincipal()
