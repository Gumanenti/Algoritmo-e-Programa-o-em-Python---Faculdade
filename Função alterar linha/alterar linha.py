arquivo = open("alterarlinha.txt", "w")

arquivo.write("Maria;sc365987;6.5 4.0 7.5")
arquivo.write("\n")
arquivo.write("Roberto;sc569874;4.5 3.0 6.0")
arquivo.write("\n")
arquivo.write("Carlos;sc222222;7.0 8.0 9.0")
arquivo.write("\n")
arquivo.write("Pedro;sc112141;9.0 6.0 10.0")
arquivo.write("\n")
arquivo.close()

def alterarElemento():
    print("-" * 30)
    arquivo = open("alterarlinha.txt", "r")
    c = 0
    lista = []
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        lista.append(dadosaluno)
        print(lista[c])
        c += 1
        print(lista)
    arquivo.close()

    a = 0
    cpfalterar = input("Digite o CPF do mecanico: ")
    while cpfalterar not in lista[a][0]:
        a += 1
    if cpfalterar in lista[a][0]:
        print("é igual")
        print(a)
        index_linha = a
        print(index_linha)
        nova_linha = "Tiagoo;sc332141;9.0 6.0 10.0"

        with open("alterarlinha.txt",'r') as arquivo:
            texto=arquivo.readlines()
            print(texto)
        with open("alterarlinha.txt", 'w') as arquivo:
            for i in texto:
                if texto.index(i)==index_linha:
                    arquivo.write(nova_linha+"\n")
                else:
                    arquivo.write(i)
        
alterarElemento()
