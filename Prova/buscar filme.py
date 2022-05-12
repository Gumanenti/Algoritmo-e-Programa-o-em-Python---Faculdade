filmes = [[1,"Homem Aranha: Longe de Casa", 2019, "Ação", ["Tom Holland", "Jake Gyllenhaal", "Zendaya"], 20.00],[2,"Vingadores: Ultimato", 2019, "Ação", ["Mark Ruffalo", "Robert Downey Jr.", "Tom Holland", "Scarlett Johansson"], 25.00 ], 
[3,"Capitão América: guerra civil", 2016, "Ação", ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson"],15.00]]

def buscar_filme(filmes):
    try:
        print("\n2 - Busca por informações de um filme específico\n")
        c = 0
        x = int(input("Digite o código do filme que deseja buscar: "))
        while x != filmes[c][0]:
            c += 1
        if x == filmes[c][0]:
            print(filmes.index(filmes[c]))
    except(IndexError):
        print("-1")

buscar_filme(filmes)
