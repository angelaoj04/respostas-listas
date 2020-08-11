notas = []
soma = 0

for i in range(4):
    nota = float((input("Informe o {}º numero: ".format(i+1))))
    notas.append(nota)
    soma = soma + nota

for i in notas:
    print(i)

print("A média das notas é: ", soma/4)

