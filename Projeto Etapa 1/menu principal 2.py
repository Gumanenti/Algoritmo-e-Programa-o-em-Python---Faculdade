def menuprincipal(lista):
    print("Menu de Opções")
    c = 0
    for item in lista:
        print(c+1,"-", lista[c])
        c += 1
    while True:
        opc = int(input("Digite a sua opção: "))
        if opc not in range(1,3):
            print("Essa opção não é válida.")
        elif opc == 1:
            print("Menu Mecânicos")
            break
        elif opc == 2:
            print("Menu Veículos")
            break

def arquivoexiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    else:
        return

def 


######## PROGRAMA PRINCIPAL ##########

arq = "listamecanicos"
lista = ["Menu Mecânicos", "Menu Veículos"]
menuprincipal(lista)
