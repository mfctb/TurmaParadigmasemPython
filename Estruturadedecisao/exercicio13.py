try:
  dia = int(input('===DIA DA SEMANA===\nDigite um Número: '))
  if dia == 1:
    print ('1-Domingo')
  elif dia == 2:
    print ('2-Segunda')
  elif dia == 3:
    print ('3-Terça')
  elif dia == 4:
    print ('4-Quarta')
  elif dia == 5:
    print ('5-Quinta')
  elif dia == 6:
    print ('6-Sexta')
  elif dia == 7:
    print ('7-Sabádo')
  else:
    print ('Número Inválido!,Tente Novamente.')
except:
   print ('Digite somente número inteiro.')