def incluirMecanico(nomeArquivo):
    cpf = input("Digite cpf: ")
    nome = input("Digite nome: ")
    datanasc = input("Digite datanasc: ")
    sexo = input("Digite sexo: ")
    salario = input("Digite salario: ")
    emails = input("Digite emails: ")
    telefones = input("Digite telefones: ")


    arquivo = open(nomeArquivo, "a")
    dadosmecanico = cpf+";"+nome+";"+datanasc+";"+sexo+";"+salario+";"+emails+";"+telefones+"\n" 
    arquivo.write(dadosmecanico)
    arquivo.close


def listarTodosMecanico(arquivoNome, mat):
    print("-" * 30)
    arquivo = open(arquivoNome, "r")
    c = 0
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        mat.append(dadosaluno)
        c += 1
        print(mat[c])

def listarUmMecanico(arquivoNome, mat):
    print("-" * 30)
    arquivo = open(arquivoNome, "r")
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        mat.append(dadosaluno)
    x = int(input("Digite o cpf: "))
    a = 0
    while x != int(mat[a][0]):
        print("é diferente")
        a += 1
    if x == int(mat[a][0]):
        print(mat[a])

def alterarMecanico(nomeArquivo, mat):
    print("-" * 30)
    arquivo = open(nomeArquivo, "r")
    c = 0
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        mat.append(dadosaluno)
        c += 1
    arquivo.close()

    a = 0
    cpfalterar = input("Digite o CPF do mecanico: ")
    while cpfalterar not in mat[a][0]:
        a += 1
    if cpfalterar in mat[a][0]:
        print("é igual")
        index_linha = a
        print(index_linha)
        cpf = input("Digite cpf: ")
        nome = input("Digite nome: ")
        datanasc = input("Digite datanasc: ")
        sexo = input("Digite sexo: ")
        salario = input("Digite salario: ")
        emails = input("Digite emails: ")
        telefones = input("Digite telefones: ")
        novos_dadosmecanicos = cpf+";"+nome+";"+datanasc+";"+sexo+";"+salario+";"+emails+";"+telefones+"\n" 

        with open(nomeArquivo,'r') as arquivo:
            texto=arquivo.readlines()
            print(texto)
        with open(nomeArquivo, 'w') as arquivo:
            for i in texto:
                if texto.index(i)==index_linha:
                    arquivo.write(novos_dadosmecanicos)
                else:
                    arquivo.write(i)
        

def excluirMecanico(arquivoNome, mat):
    print("-" * 30)
    arquivo = open("DadosMecanico.txt", "r")
    c = 0
    for linha in arquivo:
        linha = linha.replace("\n","")
        dadosaluno = linha.split(";")
        mat.append(dadosaluno)
        c += 1
    arquivo.close()

    a = 0
    cpfalterar = input("Digite o CPF do mecanico: ")
    while cpfalterar not in mat[a][0]:
        a += 1
    if cpfalterar in mat[a][0]:
        print("é igual")
        index_linha = a
        print(index_linha)
        novos_dadosmecanicos = ""

        with open(arquivoNome,'r') as arquivo:
            texto=arquivo.readlines()
            print(texto)
        with open(arquivoNome, 'w') as arquivo:
            for i in texto:
                if texto.index(i)==index_linha:
                    arquivo.write(novos_dadosmecanicos)
                else:
                    arquivo.write(i)

def carregarDoArquivo(mat, nomeArquivo):
    arquivo = open(nomeArquivo,'r')
    for linha in arquivo:
        linha = linha.replace('\n', '')
        lista = linha.split(';')
        mat.append(lista)
    print(mat)
    arquivo.close()


###################PROGRAMA_PRINCIPAL#########################333


matMecanico = []
dadosmecanico = 'DadosMecanico.txt'
listamenu = ["Menu Mecânicos", "Menu Veículos"]
listamecanico = ["Listar Todos", "Listar Elemento Específico", "Incluir Novo Mecânico", "Alterar", "Excluir Mecãnico"]
listaveiculos = ["Listar Todos Veículos", "Listar um Veículo", "Incluir Novo Veículo", "Alterar Veículo", "Excluir Veículo"]

carregarDoArquivo(matMecanico, dadosmecanico)

try:
    print("Menu de Opções")
    c = 0
    for item in listamenu:
        print(c+1,"-", listamenu[c])
        c += 1
    while True:
        opc = int(input("Digite a sua opção: "))
        if opc not in range(1,3):
            print("Essa opção não é válida.")
        elif opc == 1:
            a = 0
            for item in listamecanico:
                print(a+1,"-", listamecanico[a])
                a += 1
            mec = -1
            while mec != 0:
                mec = int(input("Digite a sua opção ou 0 para voltar: "))
                if mec not in range(0, 6):
                    print("Essa opção não é válida.")
                if mec == 0:
                    print("Menu de Opções")
                    c = 0
                    for item in listamenu:
                        print(c+1,"-", listamenu[c])
                        c += 1
                if mec == 1:
                    print(listamecanico[0])
                    listarTodosMecanico(dadosmecanico, matMecanico)
                if mec == 2:
                    print(listamecanico[1])
                    listarUmMecanico(dadosmecanico, matMecanico)
                if mec == 3:
                    print(listamecanico[2])
                    incluirMecanico(dadosmecanico)
                if mec == 4:
                    print(listamecanico[3])
                    alterarMecanico(dadosmecanico, matMecanico)
                if mec == 5:
                    print(listamecanico[4])
                    excluirMecanico(dadosmecanico, matMecanico)

                    
            
        elif opc == 2:
            print("menuveiculos(listaveiculos)")
            break
except ValueError:
    print("-" * 30)
    print("Erro. Por favor, digite uma opção correta.")
    print("-" * 30)
    menuprincipal(listamenu)


