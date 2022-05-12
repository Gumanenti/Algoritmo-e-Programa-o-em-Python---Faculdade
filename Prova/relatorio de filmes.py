filmes = [[1,"Homem Aranha: Longe de Casa", 2019, "Ação", ["Tom Holland", "Jake Gyllenhaal", "Zendaya"], 20.00],[2,"Vingadores: Ultimato", 2019, "Ação", ["Mark Ruffalo", "Robert Downey Jr.", "Tom Holland", "Scarlett Johansson"], 25.00 ], 
[3,"Capitão América: guerra civil", 2016, "Ação", ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson"],15.00]]

#**************************Relatório de Filmes**************************
    #Código do filme: 1
    #Nome: Homem Aranha: Longe de Casa
    #Ano de lançamento: 2019
    #Gênero: Ação
    #Autores: Tom Holland
    #         Jake Gyllenhaal
    #         Zendaya
    #Preço de locação: R$20.00

    #+++++++++++++++++++++++++++++++++++++
    #Código do filme: 2
    #Nome: Vingadores: Ultimato
    #...
    
def relatorio_filmes(filmes):
    print("\n*************************Relatório de Filmes**************************\n")
    for i in range(len(filmes)):
        print(f" Código do filme: {filmes[i][0]}\n Nome:{filmes[i][1]}\n Ano de Lançamento:{filmes[i][2]}\n Gênero:{filmes[i][3]}\n Ator:{filmes[i][4]}\n Preço Locação:{filmes[i][5]}\n +++++++++++++++++++++++++++++++++++++")
relatorio_filmes(filmes)
