idades = []
alturas = []
for i in range(5):
    idades.append(int(input("Informe a idade {}:  ".format(i+1))))
    alturas.append(float(input("Informe a altura {}: ".format(i+1))))

#invertendo as listas
alturas.reverse()
idades.reverse()

print("alturas:", alturas)
print("idades:",  idades)