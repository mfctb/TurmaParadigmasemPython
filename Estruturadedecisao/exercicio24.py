try:
  resultado = float
  numero1=float(input('Digite um número'))
  numero2=float(input('Digite outro número'))
  print('[ 1 + ]')
  print('[ 2 - ]')
  print('[ 3 * ]')
  print('[ 4 / ]')
  operacao=(input('que operação deseja fazer?'))
  if operacao == '1':
    resultado = numero1 + numero2
    if resultado % 2 == 0 :
      print(f'{resultado:.2f} É PAR')
      print (type(resultado))
    else:
      print(f'{resultado:.2f} É ÍMPAR')
      print (type(resultado))
    if resultado >= 0 :
      print(f'{resultado:.2f} É POSITIVO')
      
    else:
      print(f'{resultado:.2f} É NEGATIVO')
      
    
  elif operacao == '2':
    resultado = numero1 - numero2
    if resultado % 2 == 0 :
      print(f'{resultado:.2f} É PAR')
    else:
      print(f'{resultado:.2f} É ÍMPAR')
    if resultado >= 0 :
      print(f'{resultado:.2f} É POSITIVO')
    else:
      print(f'{resultado:.2f} É NEGATIVO')
    
  elif operacao == '3':
    resultado = numero1 * numero2
    if resultado % 2 == 0 :
      print(f'{resultado:.2f} É PAR')
    else:
      print(f'{resultado:.2f} É ÍMPAR')
    if resultado >= 0 :
      print(f'{resultado:.2f} É POSITIVO')
    else:
      print(f'{resultado:.2f} É NEGATIVO')
    
  elif operacao == '4':
    resultado = numero1 / numero2
    if resultado % 2 == 0 :
      print(f'{resultado:.2f} É PAR')
      
    else:
      print(f'{resultado:.2f} É ÍMPAR')
    if resultado >= 0 :
      print(f'{resultado:.2f} É POSITIVO')
    else:
      print(f'{resultado:.2f} É NEGATIVO')
      
except:
  print('Dados inválidos')