def incluirConserto(dic, nomeArquivo):
    print('Mecânicos: ')
    cpfMecanico = input('Escolha o CPF de um mecânico:')
    print('Veículos: ')
    placaVeiculo = input('Escolha a placa de um veículo:')
    dataConserto = input('Qual a data do conserto? ')
    dataSaida = str(input('Qual a data de saída? '))
    problema = str(input('Qual foi o problme? '))
    valorConserto = input('Qual o valor do conserto?')
    relatorioConserto = dataSaida+';'+problema+';'+valorConserto+''

    tupla = (cpfMecanico, placaVeiculo, dataConserto)
    dic[tupla] = [relatorioConserto]
    arquivo = open(nomeArquivo, 'a')
    conserto = cpfMecanico+';'+placaVeiculo+';'+dataConserto+';'+relatorioConserto+'\n'
    arquivo.write(conserto)
    arquivo.close()

dicConserto = {}
dadosconsertos = 'Consertos.txt'
incluirConserto(dicConserto, dadosconsertos)
print(dicConserto)
