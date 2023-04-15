try:
  print("Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual\n de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de\n crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários\n para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.")
  a = 80000
  b = 200000
  ano = 0
  
  while a <= b:
  	a += a * 0.03
  	b += b * 0.015
  	ano += 1
   
  print (f"\n   R E S P O S T A!!!\n\nA ultrapassa ou iguala a B em {ano} anos")  
except:
  print('Digite Corretamente o que se pede!')