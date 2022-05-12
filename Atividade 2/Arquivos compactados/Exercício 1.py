#Exercicio 1
palavra = str(input("Digite uma palavra: "))
letra = str(input("Digite uma letra: "))

for i in range(0, len(letra)):
    nova_string = palavra.replace(letra[i],"", 1)
    print(nova_string)
