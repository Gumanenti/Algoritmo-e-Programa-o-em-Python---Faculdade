def datanasc(mat, dataAtual):
    c = 0
    while True:
        anos = int(dataAtual[2]) - int(mat[c][2][4:])
        if int(dataAtual[1]) < int(mat[c][2][2:4]):
            anos -= 1
        if int(dataAtual[1]) == int(mat[c][2][2:4]):
            if int(dataAtual[0]) < int(mat[c][2][0:2]):
                anos -= 1

        if x <= anos:
            print(mat[c])
        c +=1
mat = [['669', 'lul', '02031993', 'fem', '400', 'lulu.m', '336655'], ['5555', 'gigi', '02041993', 'fem', '1400', 'gigi.g', '336699']]
dataAtual = ['31', '12', '2020']
x = int(input("A partir de qual idade quer listar os mecânicos? "))


datanasc(mat, dataAtual)

