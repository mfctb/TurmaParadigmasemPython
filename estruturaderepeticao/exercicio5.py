try:
  print("Supondo que a população de um país A seja 'X' habitantes com uma taxa anual\n de crescimento de 3% e que a população de B seja de 'Y' habitantes com uma taxa de\n crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários\n para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.\n \n")
  a = int (input("Digite a quantidade da população A:"))
  b = int (input("Digite a quantidade da população B:"))
  ano = 0
  
  while a <= b:
  	a += a * 0.03
  	b += b * 0.015
  	ano += 1
   
  print (f"\n   R E S P O S T A!!!\n\nO país A ultrapassa ou iguala o país B em {ano} anos")  
except:
  print('Fim do Programa!!!\nDigite Corretamente o que se pede!')