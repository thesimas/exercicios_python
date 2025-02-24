idade = int(input('Qual é a sua idade?'))   

if idade <= 18:                     #if é uma condição que irá verificar a resposta do usuario.
    print('Você é menor de idade!')

elif idade >= 18 and idade <65:     #elif serve para criar mais uma verificação além do if.
    print('Você é um adulto!')

else:                               #else irá dar a resposta quando as condições não forem verdadeiras.
    print('Você é um idoso!')

'''
 == (igual a)

!= (diferente de)

< (menor que)

> (maior que)

<= (menor ou igual a)

>= (maior ou igual a).  

'''