numeros = []

for i in range(5):
    numero = int(input("Informe o {}º numero: ".format(i+1)))
    numeros.append(numero)

numeros.reverse()

for i in numeros:
    print(i)