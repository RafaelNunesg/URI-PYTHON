x, y, z = input("Digite três números: ").split()

x = int(x)
y = int(y)
z = int(z)

maiorXY = (x + y + abs(x - y))/2
maiorXYZ = (maiorXY + z + abs(maiorXY - z))/2

print(maiorXYZ, "eh o maior")