num1 = int(input("Escreva um número: "))
cont = 0
for c in range(1, num1 + 1):
   if num1 % c == 0:
       cont += 1
if cont == 2:
    print("numero é primo")
else:
    print("numero não é primo")
