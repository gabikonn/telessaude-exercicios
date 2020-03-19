num = int(input('Digite um número: '))

if num%2==0:
    if num%4==0:
        print('O número', num,'é par e múltiplo de 4')
    else:
        print('O número', num, 'é par')
else:
    print('O número',num, 'é ímpar')

# Peça ao usuário um número. Dependendo do número ser par ou ímpar, imprima uma mensagem apropriada para o usuário. 
# Dica: como um número par / ímpar reage de maneira diferente quando dividido por 2?
