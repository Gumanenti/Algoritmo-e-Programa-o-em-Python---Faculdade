def menuprincipal(p):
    try:
        print("Menu de Opções")
        c = 0
        for item in p:
            print(c+1,"-", p[c])
            c += 1
        while True:
            opc = int(input("Digite a sua opção: "))
            if opc not in range(1,3):
                print("Essa opção não é válida.")
            elif opc == 1:
                menumecanico(listamecanico)
                break
            elif opc == 2:
                menuveiculos(listaveiculos)
                break
    except(ValueError):
        print("Deu")
