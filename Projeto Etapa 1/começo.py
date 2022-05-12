mecanico = []
cpf = int(input("Digite o CPF do mêcanico: "))
mecanico.append(cpf)

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
    maisemail = str(input("Quer digitar mais um e-mail? [S/N] "))
    if maisemail in "Nn":
        break
mecanico.append(emails)

telefones = []
while True:
    emails.append(input("Digite um telefone: "))
    maistelefone = str(input("Quer digitar mais um teelfone? [S/N] "))
    if maistelefone in "Nn":
        break
mecanico.append(emails)
print(mecanico)
