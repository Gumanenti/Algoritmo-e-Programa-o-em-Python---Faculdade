def arquivoexiste(nome):
    if a == open(nome, "rt") is True:
        a.close()
        print("Deu certo")
    else:
        print("não deu")


arquivoexiste(nome)
