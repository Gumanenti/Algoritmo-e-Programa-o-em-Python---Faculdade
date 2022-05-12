#Exercicio 9
def anagrama():
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")

    if sorted(palavra1.lower()) == sorted(palavra2.lower()):
        print("As palavras", palavra1, "e", palavra2, "formam um anagrama.")
    else:
        print("As palavras", palavra1, "e", palavra2, "não formam um anagrama.")

anagrama()

