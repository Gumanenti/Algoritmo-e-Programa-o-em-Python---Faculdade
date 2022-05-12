emails = []
while True:
    emails.append(input("Digite um e-mail: "))
    maisemail = str(input("Quer digitar mais um e-mail? [S/N] "))
    if maisemail in "Nn":
        break
print(emails)
