def mostrarMenu():
    print("Menu de Opções")
    print("1 - Realizar Entrevista")
    print("2 - Encerrar Entrevistas e Apresentar Estatísticas")

def main():
    menu =True
    while menu:
        mostrarMenu()
        opc = input("Escolha uma opção: ")
        if opc == "1":
            print("-" * 30)
            print("Você escolheu a Opção 1 - Realizar Entrevista")
            print("-" * 30)
            realizarEntrevista()
        if opc == "2":
            print("-" * 30)
            print("Você escolheu a Opção 2  - Encerrar Entrevistas e Apresentar Estatísticas")
            print("-" * 30)
            encerrarEntrevista()


def realizarEntrevista():
    linha = []
    sexo = input(str("Digite o Sexo(masculino/feminino): "))
    idade = input(str("Digite a Idade: "))
    fumante = input(str("É fumante? (sim/nao): "))
    escolaridade = input(str("Digite a escolaridade: "))
    linha.append(sexo)
    linha.append(" ")
    linha.append(idade)
    linha.append(" ")
    linha.append(fumante)
    linha.append(" ")
    linha.append(escolaridade)
    print("-" * 30)
    print("A entrevista acabou, retornando ao Menu...")
    print("-" * 30)
    arquivo = open("Pesquisa.txt","a")
    arquivo.writelines(linha)
    arquivo.write("\n")
    arquivo.close()

def encerrarEntrevista():
    arquivo = open("Pesquisa.txt", "r")
    lista = []
    for linha in arquivo:
        linha = linha.replace("\n", "")
        linha = linha.split(" ")
        lista.append(linha) 

    #['feminino', '28', 'não', 'superior']
    homem = 0
    mulher = 0
    fumante = 0
    homemNãoFumanteMenor40 = 0
    mulherFumanteMaior40 = 0

    for i in range(len(lista)):
        if str(lista[i][0]) in "masculino":
            homem += 1

    for i in range(len(lista)):
        if str(lista[i][0]) in "feminino":
            mulher += 1
    
    for i in range(len(lista)):
        if str(lista[i][2]) in "sim":
            fumante += 1

    percentualfumantes = int(fumante) / len(lista)
    print("O percentual de fumantes é de", percentualfumantes * 100, "%")

    for i in range(len(lista)):
        if str(lista[i][0]) in "masculino" and str(lista[i][2]) in "não" and int(lista[i][1]) < 40:
            homemNãoFumanteMenor40 += 1
    percentualHomemNãoFumanteMenor40 = int(homemNãoFumanteMenor40) / int(homem)
    print("O percentual de homens não fumantes abaixo de 40 anos é de", percentualHomemNãoFumanteMenor40 * 100, "%")

    for i in range(len(lista)):
        if str(lista[i][0]) in "feminino" and str(lista[i][2]) in "sim" and int(lista[i][1]) >= 40:
            mulherFumanteMaior40 += 1
    percentualmulherFumanteMaior40 = int(mulherFumanteMaior40) / int(mulher)
    print("O percentual de mulheres fumantes acima de 40 anos é de", percentualmulherFumanteMaior40 * 100, "%")
    print("-" * 30)
    
#######################PROGRAMA_PRINCIPAL################################
            
main()
        
