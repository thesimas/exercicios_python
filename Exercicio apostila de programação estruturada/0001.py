#Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00.
#  Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area=float(input('Quantos metros quadrados serão pintados?'))
litro= 3 
lata= 18
valor_lata=int(80)

calculo1=float(area)*int(litro)/int(lata) 
calculo2=float(calculo1)*int(valor_lata)

print('Quantidade de latas:', calculo1)
print('valor das latas:', calculo2)


#não consegui fazer a conta correta :(
