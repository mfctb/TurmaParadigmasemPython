try:
  letra = str(input('informe F para feminino ou  M para masculino ')).upper()
  if letra == 'F':
    print('F - FEMININO')
  elif  letra == 'M':
    print('M - MASCULINO')
  else:
    print('Tente Novamente!')
except:
  print("Dados incorretos!,tente novamente!")
  