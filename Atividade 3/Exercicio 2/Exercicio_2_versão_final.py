arquivo = open("Votos.txt", "w")

arquivo.write("500")
arquivo.write("\n")
arquivo.write("400")
arquivo.write("\n")
arquivo.write("400")
arquivo.write("\n")
arquivo.write("500")
arquivo.write("\n")
arquivo.write("100")
arquivo.write("\n")
arquivo.write("200")
arquivo.write("\n")
arquivo.write("500")
arquivo.write("\n")
arquivo.write("400")
arquivo.write("\n")
arquivo.write("500")
arquivo.write("\n")
arquivo.write("400")
arquivo.write("\n")
arquivo.write("300")
arquivo.write("\n")
arquivo.write("1050")
arquivo.write("\n")
arquivo.write("100")
arquivo.write("\n")
arquivo.write("12")
arquivo.write("\n")
arquivo.write("300")
arquivo.write("\n")
arquivo.write("57")
arquivo.write("\n")
arquivo.write("500")
arquivo.write("\n")
arquivo.write("500")
arquivo.write("\n")
arquivo.write("100")
arquivo.write("\n")
arquivo.write("200")
arquivo.write("\n")
arquivo.write("400")
arquivo.write("\n")
arquivo.write("300")
arquivo.write("\n")
arquivo.write("1050")
arquivo.write("\n")
arquivo.write("100")
arquivo.write("\n")
arquivo.write("12")
arquivo.write("\n")
arquivo.write("300")
arquivo.write("\n")
arquivo.write("57")
arquivo.write("\n")
arquivo.close()

arquivo = open("Votos.txt", "r")
lista = []
for linha in arquivo:
    linha = linha.replace("\n", "")
    lista.append(linha) 

votos500 = 0
votos400 = 0
votos300 = 0
votos200 = 0
votos100 = 0
votosnulos = 0
for i in range(len(lista)):
    if lista[i] == "500":
        votos500 += 1
    if lista[i] == "400":
        votos400 += 1
    if lista[i] == "300":
        votos300 += 1
    if lista[i] == "200":
        votos200 += 1
    if lista[i] == "100":
        votos100 += 1
    if lista[i] != "500" and lista[i] != "400" and lista[i] != "300" and lista[i] != "200" and lista[i] != "100":
        votosnulos += 1
listaquantidade = []
listaquantidade.append(votos500)
listaquantidade.append(votos400)
listaquantidade.append(votos300)
listaquantidade.append(votos200)
listaquantidade.append(votos100)

maior = listaquantidade[0]
i = 0
while i < len(listaquantidade):
    if listaquantidade[i] > maior:
        maior = listaquantidade[i]
    i += 1
if maior == listaquantidade[0]:
    print("-" * 30)
    print("O candidato de código 500 é o mais votado com", maior, "votos")
if maior == listaquantidade[1]:
    print("-" * 30)
    print("O candidato de código 400 é o mais votado com", maior, "votos")
if maior == listaquantidade[2]:
    print("-" * 30)
    print("O candidato de código 300 é o mais votado com", maior, "votos")
if maior == listaquantidade[3]:
    print("-" * 30)
    print("O candidato de código 200 é o mais votado com", maior, "votos")
if maior == listaquantidade[4]:
    print("-" * 30)
    print("O candidato de código 100 é o mais votado com", maior, "votos")

menor = listaquantidade[0]
i = 0
while i < len(listaquantidade):
    if listaquantidade[i] < menor:
        menor = listaquantidade[i]
    i += 1
if menor == listaquantidade[0]:
    print("O candidato de código 500 é o mais votado com", menor, "votos")
if menor == listaquantidade[1]:
    print("O candidato de código 400 é o mais votado com", menor, "votos")
if menor == listaquantidade[2]:
    print("O candidato de código 300 é o mais votado com", menor, "votos")
if menor == listaquantidade[3]:
    print("O candidato de código 200 é o mais votado com", menor, "votos")
if menor == listaquantidade[4]:
    print("O candidato de código 100 é o mais votado com", menor, "votos")

print("A quantidade de votos nulos é de", votosnulos, "votos")
print("-" * 30)

arquivo.close()

