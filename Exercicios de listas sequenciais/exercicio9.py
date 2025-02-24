# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Qual é a sua altura?'))

peso_ideal_homem = float(72.7)*float(altura)-int(58)
peso_ideal_mulher = float(62.1)*float(altura)-float(44.7)

print('Caso você seja Homem, seu peso idel é:', peso_ideal_homem, 'kilos.')
print('Caso você seja Mulher, seu peso idel é:', peso_ideal_mulher, 'kilos.')
