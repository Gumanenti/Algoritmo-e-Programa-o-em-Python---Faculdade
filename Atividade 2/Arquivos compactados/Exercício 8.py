#Exercicio 8
frase = str(input("Digite uma frase: "))

letra_a = frase.count("a") + frase.count("A")
letra_e = frase.count("e") + frase.count("E")
letra_i = frase.count("i") + frase.count("I")
letra_o = frase.count("o") + frase.count("O")
letra_u = frase.count("u") + frase.count("U")
espaço = frase.count(" ")

print("Quantidade que aparece a vogal A: ", letra_a)
print("Quantidade que aparece a vogal E: ", letra_e)
print("Quantidade que aparece a vogal I: ", letra_i)
print("Quantidade que aparece a vogal O: ", letra_o)
print("Quantidade que aparece a vogal U: ", letra_u)
print("Quantidade de espaços: ", espaço)
