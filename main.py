try:
  numero = float(input('Digite um número: '))
  if numero == round(numero):
    print("Inteiro")
  else:
    print("Decimal")
except:
  print('Dados inválidos!')