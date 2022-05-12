arquivo = open("OlaArquivo.txt", "r")

for i in range(1):
    x = arquivo.readline() #como se o python estivesse lendo com os olhos, a proxima leitura começa onde esse terminou
    print(x)
arquivo.close

y = arquivo.readlines() #cria uma lista com as palavras
print(y)
