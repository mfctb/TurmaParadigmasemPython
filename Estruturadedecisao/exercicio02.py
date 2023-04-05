try:
  numero = float (input('informe um número'))
  if numero < 0:
    print (f'{numero} é negativo')
  else:
    print(f'{numero} é positivo')
except:
  print("Dados incorretos!,tente novamente!")
  