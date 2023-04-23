numeros = input("Digite três números: ").split()

for i in range(3):
    maior = (int(numeros[i]) + int(numeros[i+1]) + abs(int(numeros[i]) - int(numeros[i+1])))/2

    print(maior)