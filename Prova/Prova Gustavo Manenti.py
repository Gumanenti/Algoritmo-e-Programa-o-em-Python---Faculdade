# PROVA PRÁTICA ONLINE DE AP1S1 - II SEM/2020 - 21/12/2020

#DESCRIÇÃO DA PROVA

#Escreva um código Python modularizado seguindo a estrutura do programa principal e das funções,
#conforme o código a seguir, respeitando as passagens de parâmetros nas funções inclusive.
#O objetivo do programa proposto é gerenciar os filmes de uma locadora virtual. As prinicipais funções
#a serem implementadas estão definidas na função mostrarMenu().
#O programa inicializará com uma lista de Filmes (definida na função main()), que tem a seguinte estrutura:
#Filmes = [[Código, Nome, AnoLançamento, Gênero, [Ator1, Ator2,...,Atorn], PreçoLocação], 
#       ...,[Código, Nome, AnoLançamento, Gênero, [Ator1, Ator2,..., Atorn], PreçoLocação]]

#=====================================================================
#Esta função está pronta e apresenta o menu de opções para o usuário fazer a sua escolha
def mostrarMenu():
    print("\n\nLocadora de Filmes:\n")
    print("1 - Inserir novo filme")
    print("2 - Buscar um filme")
    print("3 - Remover filme")
    print("4 – Gerar relatório de filmes")
    print("5 – Buscar filmes de um ator específico")
    print("6 - Sair")

#=====================================================================
#QUESTÃO 1 (1.5) - Implemente aqui o código da função inserir_filme(), que receberá como parâmetro uma referência para
# a lista Filmes (definida na main()) e deverá solicitar e incluir os dados de um filme nessa lista.    
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
    

        
#=====================================================================
#QUESTÃO 2 (1.5) - Implemente o código da função buscar_filme(), que receberá como parâmetro uma referência para
# a lista Filmes e o código do filme a ser procurado. A função deverá retornar o índice da posição
# do filme na lista, se ele estiver cadastrado. Caso o filme não seja encontrado, a função deverá retornar -1.
#Os dados do filme procurado deverão ser impressos na função main(). Caso o filme não tenha sido localizado,
# a função main() deverá imprimir a mensagem informando que o filme não está cadastrado.
def buscar_filme(filmes, codigo_filme):
    try:
        print("\n2 - Busca por informações de um filme específico\n")
        c = 0
        while codigo_filme != filmes[c][0]:
            c += 1
        if codigo_filme == filmes[c][0]:
            print("Índice de posição do filme na lista:", filmes.index(filmes[c]))
    except(IndexError):
        print("-1")
    
#=====================================================================
#QUESTÃO 3 (1.5) - Implemente o código da função remover_filme(), que receberá como parâmetro uma referência para
# a lista Filmes e o código do filme a ser removido. Essa função deverá chamar a função buscar_filme(), para
# verificar se o mesmo existe na lista e recuperar a sua posição para remoção.
#A função deverá imprimir uma mensagem informando que o filme foi removido com sucesso.
#Caso o filme não tenha sido encontrado, deverá imprimir a mensagem informando que o filme não está cadastrado.
def remover_filme(filmes, codigo_filme):    
    print("\n3 - Remoção de um filme com todas suas informações\n")
    try:
        c = 0
        while codigo_filme != filmes[c][0]:
            c += 1
        if codigo_filme == filmes[c][0]:
            filmes.remove(filmes[c])
            print("Filme removido com sucesso.")
            print(filmes)
    except(IndexError):
        print("Filme não cadastrado.")

        
    
#=====================================================================
#QUESTÃO 4 (2.0) - Implemente o código da função relatorio_filmes(), que receberá como parâmetro uma referência para
# a lista Filmes e imprimirá os dados de cada filme de acordo com o formato a seguir:
    
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

    
#=====================================================================
#QUESTÃO 5 (2.0) - Implemente o código da função buscar_filmes_ator_especifico(), que receberá como parâmetro uma referência para
# a lista Filmes e o nome de um ator. Essa função deverá buscar e apresentar o nome e o ano de lançamento de todos os filmes
#que tenham a participação de um ator específico fornecido pelo usuário.
#Caso não exista filmes com a participação do ator desejado, a função deverá imprimir uma mensagem informando que não há
#filmes com esse ator cadastrado.
def buscar_filmes_ator_especifico(filmes, nome_ator):    
    print("\n5 - Busca por filmes de um ator específico\n")
    try:
        a = 0
        while True:
            if nome_ator in filmes[a][4]:
                print(filmes[a][1:3])
                a += 1
            elif nome_ator not in filmes[a][4]:
                a += 1
                if nome_ator in filmes[a][4]:
                    print(filmes[a][1:3])
                    a += 1
    except(IndexError):
        print("")
    
#=====================================================================

#Função principal que usa as funções definidas anteriormente
# QUESTÃO 6 (1.5) - Inclua aqui as chamadas das funções respeitando os parâmetros e tratando corretamente
# o valor de retorno (quando houver).
def main():
    filmes = [[1,"Homem Aranha: Longe de Casa", 2019, "Ação", ["Tom Holland", "Jake Gyllenhaal", "Zendaya"], 20.00],[2,"Vingadores: Ultimato", 2019, "Ação", ["Mark Ruffalo", "Robert Downey Jr.", "Tom Holland", "Scarlett Johansson"], 25.00 ], 
[3,"Capitão América: guerra civil", 2016, "Ação", ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson"],15.00]]
     
    menu=True
    while menu:
        mostrarMenu()
        opc=input("\nEscolha uma opção: ")
        if opc == '1':
            #INCLUA AQUI A CHAMADA DA FUNÇÃO inserir_filme() COM O(S) PARÂMETRO(S) NECESSÁRIO(S)
            inserir_filme(filmes)
        elif opc == '2':
            codigo_filme=int(input("Digite o código do filme que deseja consultar: "))      		
            #INCLUA AQUI A CHAMADA DA FUNÇÃO buscar_filme() COM O(S) PARÂMETRO(S) NECESSÁRIO(S),
            #TRATANDO CORRETAMENTE O VALOR DE RETORNO
            buscar_filme(filmes, codigo_filme)
        elif opc == '3':
            codigo_filme=int(input("Digite o código do filme que deseja remover: "))
            #INCLUA AQUI A CHAMADA DA FUNÇÃO remover_filme() COM O(S) PARÂMETRO(S) NECESSÁRIO(S)            
            remover_filme(filmes, codigo_filme)    
        elif opc == '4':
            #INCLUA AQUI A CHAMADA DA FUNÇÃO relatorio_filmes() COM O(S) PARÂMETRO(S) NECESSÁRIO(S)
            relatorio_filmes(filmes)

        elif opc == '5':
            nome_ator=input("Digite o nome do ator que deseja recuperar os filmes do qual ele participou: ")
            #INCLUA AQUI A CHAMADA DA FUNÇÃO buscar_filmes_ator_especifico() COM O(S) PARÂMETRO(S) NECESSÁRIO(S)
            buscar_filmes_ator_especifico(filmes, nome_ator)
        else:
            print("\nTerminando a execução do programa!!!")
            menu=False

#===================================================================================	

########################## PROGRAMA PRINCIPAL ######################################
main()
