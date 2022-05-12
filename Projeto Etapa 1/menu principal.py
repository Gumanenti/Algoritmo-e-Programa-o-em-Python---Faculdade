def menuprincipal():
    menumecanico = str(input("Você quer acessar o Menu Mecânicos? [S/N]"))
    if menumecanico in "Nn":
        print("Entendido.")
    else:
        acessomecanico()

    menuveiculos = str(input("Você quer acessar o Menu Veículos? [S/N]"))
