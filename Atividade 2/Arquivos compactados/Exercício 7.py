#Exercicio 7 

palavra = str(input("Digite seu nome: ")).upper().strip()
inverso = ""

for letra in range(len(palavra) - 1, -1, -1):
    inverso += palavra[letra]
print("O inverso do seu nome é: ", inverso.upper())
