mat = []
arquivo = open("Dados_CEP_MRJ_covid_2019.txt", "r")
for linha in arquivo:
    linha = linha.replace("\n","")
    linhamecanico = linha.split(";")
    mat.append(linhamecanico)
print(mat[1][4])

i = 1
mortes = 0
while mat[i][4] in "OBITO":
    mortes += 1
    i += 1
print(mortes)
