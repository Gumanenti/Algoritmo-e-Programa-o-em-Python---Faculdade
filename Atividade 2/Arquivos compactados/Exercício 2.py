#Exercicio 2
palavra = str(input("Digite uma palavra: "))
letra = str(input("Digite uma letra: "))

for i in range(0, len(letra)):
    nova_string = palavra.replace(letra[i],"")
    print(nova_string)
