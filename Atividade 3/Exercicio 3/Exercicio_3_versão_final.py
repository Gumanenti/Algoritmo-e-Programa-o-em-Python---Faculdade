arquivo = open("Notas_AP1S1.txt", "w")

arquivo.write("Maria sc365987 6.5 4.0 7.5")
arquivo.write("\n")
arquivo.write("Roberto sc569874 4.5 3.0 6.0")
arquivo.write("\n")
arquivo.write("Carlos sc222222 7.0 8.0 9.0")
arquivo.write("\n")
arquivo.write("Pedro sc112141 9.0 6.0 10.0")
arquivo.write("\n")
arquivo.close()

def mediaaluno():
    print("-" * 30)
    arquivo = open("Notas_AP1S1.txt", "r")
    for linha in arquivo:
        linha = linha.replace("\n","")
        print(linha)
        dadosaluno = linha.split()
        lista.append(dadosaluno)
        print(lista)

    for i in range(len(lista)):
        soma = float(lista[i][2]) + float(lista[i][3]) + float(lista[i][4])
        media = soma/3
        lista[i].append(media)
        print("A média do aluno(a)", lista[i][0], "é igual a: ", lista[i][5])

def aprovadosounao():
    naopassou = 0
    passou = 0
    ifa = 0
    for i in range(len(lista)):
        if float(lista[i][5]) >= 6:
            passou += 1
        elif float(lista[i][5]) < 4:
            naopassou += 1
        elif float(lista[i][5]) >= 4 and float(lista[i][5]) < 6:
            ifa += 1
            
    print("Quantidade de alunos aprovados: ", passou)
    print("Quantidade de alunos não aprovados: ", naopassou)
    print("Quantidade de alunos que farão IFA: ", ifa)
    print("-" * 30)

####################_PROGRAMA_PRINCIPAL_######################
lista = []
mediaaluno()
aprovadosounao()
