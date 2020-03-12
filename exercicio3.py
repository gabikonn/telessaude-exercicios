num = int(input('Digite um número: '))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for x in a:
    if (x < num):
        b.append(x)
print(b)

print("\nLista")
for x in a:
    print(x)

print("\nRange")
for x in range(0, len(a)):
    print(x)
