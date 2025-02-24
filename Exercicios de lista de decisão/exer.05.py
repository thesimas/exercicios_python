'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota1=float(input('Qual foi sua primeira nota?\n'))
nota2=float(input('Qual foi sua segunda nota?\n'))

media =float(nota1 + nota2) / 2 

print('Sua média foi:\n', media)

if media >= 7 and media <=9: 
    print('Você está aprovado!')

elif media == 10: 
    print('Você passou com sobra!')

else: 
    print('Infelizmente foi reprovado.')

