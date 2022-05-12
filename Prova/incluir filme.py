filmes = [[1,"Homem Aranha: Longe de Casa", 2019, "Ação", ["Tom Holland", "Jake Gyllenhaal", "Zendaya"], 20.00],[2,"Vingadores: Ultimato", 2019, "Ação", ["Mark Ruffalo", "Robert Downey Jr.", "Tom Holland", "Scarlett Johansson"], 25.00 ], 
[3,"Capitão América: guerra civil", 2016, "Ação", ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson"],15.00]]

def inserir_filme(filmes):
    print("\n1 - Cadastro de novo filme\n")
    cod = int(input("Digite o Código do filme que deseja inserir: "))
    while cod != "":
        filme = []
        filme.append(cod)
        nomefilme = str(input("Digite o nome do filme: "))
        filme.append(nomefilme)
        anolanc = str(input("Digite o ano de lançamento do filme: "))
        filme.append(anolanc)
        genero = str(input("Digite o genero do filme: "))
        filme.append(genero)
        atores = []
        while True:
            atores.append(str(input("Digite o nome de um ator do filme: ")))
            maisatores = str(input("Quer adicionar mais um ator? [S/N]"))
            if maisatores in "Nn":
                break
        filme.append(atores)
        preçolocaçao = float(input("Digite o preço de locação: "))
        filmes.append(filme)
        print(filmes)
        cod = str(input("Digite o código de um novo filme ou digite enter para encerrar."))

inserir_filme(filmes)
