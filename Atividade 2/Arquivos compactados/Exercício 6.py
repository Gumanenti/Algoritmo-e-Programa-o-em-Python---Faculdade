#Exercicio6 
nome = str(input("Digite seu nome: "))

i = 0
for i in range(len(nome)):
    print(nome[:i+1])
    i += 1
