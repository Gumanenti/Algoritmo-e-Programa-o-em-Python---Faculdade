def encontrarMarca(mat):
    c = 0
    x = input("Digite a marca que deseja listar: ")
    while True:
        if x in mat[c][2]:
            print(mat[c])
        c += 1

mat = [['pzm5075', 'hatch', 'fiat', 'uno', '1997', '4', 'flex', 'branco'], ['ola8600', 'sedan', 'ford', 'ka', '2001', '2', 'alcool', 'cinza']]

encontrarMarca(mat)
