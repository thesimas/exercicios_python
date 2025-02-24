#Faça um Programa que peça dois números e imprima o maior deles.

numb_1=int(input('Me informe um número.'))
numb_2=int(input('Me informe outro número.'))

if numb_1 > numb_2: 
    print('O primeiro numero informado é maior que o segundo.')
elif numb_2 > numb_1:
    print('O segundo numero informado é maior que o primeiro.')
else: 
    print('Os numero informados são iguais.')
