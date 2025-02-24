#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra=input('Me informe uma letra.''\n').strip().upper() #.strip remove caracter vazio.

if letra in ('A','E','I','O','U'):     #caso queira que essa condição atenda esse conjunto, se utiliza o IN.
    print('A letra informada é vogal.')

else:
    print('A letra informada é consoante.')