try:
  numero1 = float (input('Digite um numero'))
  numero2 = float (input('Digite outro numero'))
  if numero1 > numero2:
    print(f'O número {numero1} é maior que o {numero2}')
  elif numero1 < numero2:
    print(f'O número {numero1 } é menor que o {numero2}')
  else:
    print('valor invalido!')
except:
    print("Dados incorretos!,tente novamente!")