vetor = []
par = []
impar = []

for i in range(20):
    vetor.append(int(input("Informe o {}º número: ".format(i+1))))
    if vetor[i]%2 == 0:
        par.append(vetor[i])
    else:
        impar.append(vetor[i])

print("Vetor final: ", vetor)

print("\nVetor par: ", par)

print("\nVetor ímpar: ", impar)