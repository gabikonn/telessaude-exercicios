from random import randint

sair = ""
cont = 0
aleatorio = randint(1, 9)

while sair != "exit":
    sair = input('Adivinhe um número entre 1 e 9: ')
    if sair != "exit":
        num = int(sair)
        if aleatorio == num:
            print('Acertou!')
            break
        elif aleatorio < num:
            print('Muito baixo!')
        else:
            print('Muito alto')
        cont += 1

print("Tentativas: ", cont)

print("O número é:", aleatorio)
