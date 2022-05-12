f=input("Digite a frase: ")

l=input("Digite a letra: ")

idx=f.find(l)

print(f[:idx]+f[idx+1:])
