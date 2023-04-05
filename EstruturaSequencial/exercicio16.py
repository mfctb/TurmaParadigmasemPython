print('Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.')
areapintada = float (input('Quantos metros quadrados serão pintados?'))
#litrotinta = 18
cobertura = areapintada / 3
precotinta = 80
precototal = 
quantidadetinta = 0
if areapintada>= 18:
  quantidadetinta = 





tamanho = float(input('Tamanho em metros quadrados: '))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('%d latas' %latas)
print ('R$ %.2f' %preco)