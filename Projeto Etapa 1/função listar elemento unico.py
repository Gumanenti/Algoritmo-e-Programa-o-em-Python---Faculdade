def listarumelemento(p):
    a = 0
    x = int(input("Digite um numero"))
    while x != p[a][0]:
        a += 1
    if x == p[a][0]:
        print(p[a])



lista = [[1, 2, 3], [4, 5, 6]]
listarumelemento(lista)
