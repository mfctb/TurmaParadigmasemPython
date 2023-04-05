try:
  numero = int(input('Digite um inteiro: '))
  
  if (numero%2) == 0:
      print("Par")
  else:
      print("Ímpar")
except:
  print('Digite corretamente o que se pede')
