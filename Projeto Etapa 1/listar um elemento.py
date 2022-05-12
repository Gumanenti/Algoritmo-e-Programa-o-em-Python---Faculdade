def listarumelemto(p):
    x = int(input("Digite o CPF do mecânico: "))
    if x in galera:
        elemento = p.index(x)
        print(elemento)
