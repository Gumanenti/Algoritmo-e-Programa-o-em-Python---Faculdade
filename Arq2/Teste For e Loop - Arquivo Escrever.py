arquivo = open("OlaArquivo.txt", "w")

arquivo.write("Eu estou aqui")
arquivo.write("\n")
arquivo.writelines(["1", "2", "3", "4"])
arquivo.write("\n")
arquivo.write("Eu sou o Gustavo")

arquivo.close()
