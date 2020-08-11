vetor = []
consoantes = []

for i in range(10):
    vetor.append(input("Informe a letra: "))

for letra in vetor:
    if "aeiou".find(letra) == -1:
        consoantes.append(letra)

print(consoantes)