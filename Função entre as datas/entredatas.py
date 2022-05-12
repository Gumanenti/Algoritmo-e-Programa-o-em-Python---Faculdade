
mat = [['393', 'pzm5075', '05032020', '05042020', 'cambio', '5000'], ['555', 'xos4938', '05022020', '30022020', 'motor', '6500']]
dataPartir = ['31', '01', '2020']
dataAte = ['31', '10', '2020']

print(mat[0][2][4:])
if dataPartir[2] <= mat[0][2][4:] and dataAte[2] >= mat[0][2][4:]:
    if dataPartir[1] <= mat[0][2][2:4] and dataAte[1] >= mat[0][2][2:4]:
        print(mat[0])
    if dataPartir == mat[0][2][2:4]:
        if dataPartir[0] <= mat[0][2][0:2]:
            print(mat[0])
