x = int(input('Digite um número: '))
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade:'))

tempo = 100 - idade
ano = tempo + 2020

my_string = nome, "você fará 100 anos em ", ano

for i in range (x):
    print(my_string,"\n")

# Crie um programa que solicite ao usuario que digite seu nome e idade. 
# Imprima uma mensagem enderecada a eles informando o ano em que completarao 100 anos (100 - idade = resultado / resultado + 2020).
