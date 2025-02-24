#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo =str(input('Qual é o seu sexo?\n')).upper() #.upper aumenta os caracteris para maiusculo, independente do que o usuario digitar.

if sexo == str('F'): 
    print('Você é do sexo feminino!')

elif sexo == str('M'):
    print('Você é do sexo masculino')

else:
    print('Sexo inválido')

