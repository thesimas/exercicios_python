print('Irei calcular o seu faturamento de hoje!')

quant_paes=int(input('Quantos pães você vendeu hoje?'))
quant_broas=int(input('Quantas broas você vendeu hoje?'))

preco_paes=float(0.12)*(quant_paes)
preco_broas=float(1.50)*(quant_broas)

total=float(preco_paes)+float(preco_broas)
poupanca=(total)%90


print('Você arrecadou',total,'e deverá guardar',poupanca,'reais.')
