num1 = int(input("Digite a base: "))
num2 = int(input("Digite o expoente: "))

cont = 0
prod = 1
while cont < num2:
    prod = prod * num1
    cont = cont + 1

print(num1, "elevado a", num2, "=", prod)
