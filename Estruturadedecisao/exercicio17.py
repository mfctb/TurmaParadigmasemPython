try:
  ano = int(input('Digite um ano para verificar se ele é ou não bissexto: '))
        
  if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('ano bissexto')
  else:
    print('não é bissexto')
      
except:
  print('dados incorretos')