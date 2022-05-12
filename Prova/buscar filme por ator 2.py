filmes = [[1,"Homem Aranha: Longe de Casa", 2019, "Ação", ["Tom Holland", "Jake Gyllenhaal", "Zendaya"], 20.00],[2,"Vingadores: Ultimato", 2019, "Ação", ["Mark Ruffalo", "Robert Downey Jr.", "Tom Holland", "Scarlett Johansson"], 25.00 ], 
[3,"Capitão América: guerra civil", 2016, "Ação", ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson"],15.00]]

def buscar_filmes_ator_especifico(filmes):
    try:
        print("\n5 - Busca por filmes de um ator específico\n")
        a = 0
        x = str(input("Digite o nome do ator que deseja buscar: "))
        while True:
            if x in filmes[a][4]:
                print(filmes[a][1:2])
                a += 1
            elif x not in filmes[a][4]:
                a += 1
                if x in filmes[a][4]:
                    print(filmes[a][1:2])
                    a += 1
            else:
                print("Deu")
                
    except(IndexError):
        print("")

buscar_filmes_ator_especifico(filmes)
