try:
  lista = list()
  soma = 0
  multiplicacao = 1
  
  for indice in range(5):
      numero = int(input("Digite um número inteiro: "))
      lista.append(numero)
      soma += numero
      multiplicacao *= numero
  
  print("Números: ", lista)
  print("Soma: ", soma)
  print("Multiplicação: ", multiplicacao)
      
except ValueError:
  print('Digite somente números')