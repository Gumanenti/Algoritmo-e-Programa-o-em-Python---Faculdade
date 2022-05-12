#Exercicio 10
def contador(n):
    contagem = len(str(n))
    return contagem
n = int(input("Informe um número inteiro: "))
if n > 0:
    print("O número", n, "possui", contador(n), "dígitos.")
else:
    print("O número", n, "possui", contador(n) - 1, "dígitos.")
