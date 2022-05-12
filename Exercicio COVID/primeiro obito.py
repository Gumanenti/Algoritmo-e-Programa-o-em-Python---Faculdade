mat = []
arquivo = open("Dados_CEP_MRJ_covid_2019.txt", "r")
for linha in arquivo:
    linha = linha.replace("\n","")
    linhamecanico = linha.split(";")
    mat.append(linhamecanico)

