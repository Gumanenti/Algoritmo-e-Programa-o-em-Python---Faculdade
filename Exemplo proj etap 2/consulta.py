def criarMenu():
    print("Menu")
    print('1 - cadastrar medico')
    print('2 - listar medicos')
    print('3 - cadastrar paciente')
    print('4 - listar pacientes')
    print('5 - cadastrar consulta')
    print('6 - listar consulta')

def cadastrarMedico(mat):
    medico = []
    crm = input('Digite o crm: ')
    nome = input('Digite o nome do medico: ')
    medico.append(crm)
    medico.append(nome)
    mat.append(medico)

def cadastrarPaciente(mat):
    paciente = []
    cpf = input('Digite o cpf: ')
    nome = input('Digite o nome do paciente: ')
    paciente.append(cpf)
    paciente.append(nome)
    mat.append(paciente)

def listar(mat):
    qtdd = len(mat)
    for i in range(qtdd):
        print(mat[i])

def salvarConsulta(cpf, crm, data,prontuario, dic,nomeArquivo):
    tupla = (cpf, crm, data)
    dic[tupla] = [prontuario]
    arquivo = open(nomeArquivo, 'a')
    consulta = cpf+';'+crm+';'+data+';'+prontuario+'\n'
    arquivo.write(consulta)
    arquivo.close()


def salvarMatrizNoArquivo(mat, nomeArquivo):
    arquivo = open(nomeArquivo,'w')
    qtddLinhas = len(mat)
    for i in range(qtddLinhas):
        lista = mat[i]  #['1212', 'andre']  -> 1212;andre
        linha = ""
        for elemento in lista:
            linha = linha + elemento+";"
        linha = linha[:len(linha)-1]
        linha = linha+ '\n'
        arquivo.write(linha)
    arquivo.close()


def carregarConsultas(dic,nomeArquivo):
    arquivo = open(nomeArquivo,'r')
    for linha in arquivo:
        linha = linha.replace('\n','')
        dados = linha.split(';')
        tupla = (dados[0],dados[1],dados[2])
        dic[tupla] = dados[3]
    arquivo.close()

def exibirConsultas(dic,matP,matM):
#{('333', '33', '25/01/2021'): 'dor de cabeça'}
    cont = 1
    for chave in dic.keys():
        cpfPaciente = chave[0]
        crmMedico = chave[1]
        print('Consulta #' + str(cont))
        print('Paciente: ' + buscarNomePaciente(matP,cpfPaciente))
        print('Medico : ' + buscarNomeMedico(matM, crmMedico))
        print('Data consulta :' + chave[2])
        pront = dic[chave]
        print(pront)
        cont = cont + 1
       # print('Prontuario: ' + pront)



def buscarNomePaciente(mat,cpf):
    qtdd = len(mat)
    for i in range(qtdd):
        if mat[i][0] == cpf:
            return mat[i][1]
    return 'erro'

def buscarNomeMedico(mat,crm):
    for i in range(len(mat)):
        if mat[i][0] == crm:
            return mat[i][1]
    return 'erro'

#variáveis globais
matMedico = []
matPaciente = []
dicConsulta = {}
qtddMedico = 0
qtddPaciente = 0
arqPacientes = 'Pacientes.txt'
arqMedicos = 'Medicos.txt'
arqConsultas = 'Consultas.txt'

carregarDoArquivo(matMedico, arqMedicos)
carregarDoArquivo(matPaciente, arqPacientes)
carregarConsultas(dicConsulta, arqConsultas)
opcao = -1
while opcao !=0:
    criarMenu()
    opcao = int(input('Digite uma opcao : '))
    if opcao == 1:
        cadastrarMedico(matMedico)
        salvarMatrizNoArquivo(matMedico,arqMedicos)
    elif opcao == 2:
        listar(matMedico)
    elif opcao ==3:
        cadastrarPaciente(matPaciente)
        salvarMatrizNoArquivo(matPaciente,arqPacientes)
    elif opcao ==4:
        listar(matPaciente)
    elif opcao ==5:
        print('PACIENTES: ')
        listar(matPaciente)
        cpfPaciente = input('Escolha o cpf de um paciente:')
        print('MEDICOS: ')
        listar(matMedico)
        crmMedico = input('Escolha o crm do médico que fará o atendimento:')
        dataConsulta = input('Qual a data da consulta? ')
        prontuarioMed = input('Qual o prontuario do paciente? ')
        salvarConsulta(cpfPaciente, crmMedico, dataConsulta,prontuarioMed, dicConsulta,arqConsultas)
    elif opcao == 6:
        print(dicConsulta)
        exibirConsultas(dicConsulta,matPaciente,matMedico)





