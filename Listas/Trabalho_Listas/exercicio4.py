try:
  lista1 = list()
  lista2 = list()
  lista3 = list()
  
  print("Digite os elementos da primeira lista:")
  for indice in range(10):
      lista1.append(input())
  
  print("Digite os elementos da segunda lista:")
  for indice in range(10):
      lista2.append(input())
  
  for indice in range(10):
      lista3.append(lista1[indice])
      lista3.append(lista2[indice])
  
  print("A terceira lista gerada é:", lista3)
     
except ValueError:
  print('Digite somente números')