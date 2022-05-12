#Exercicio 4 

palavra = str(input("Digite uma palavra: ")).upper().strip()
inverso = ""

for letra in range(len(palavra) - 1, -1, -1):
    inverso += palavra[letra]
if inverso == palavra:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
