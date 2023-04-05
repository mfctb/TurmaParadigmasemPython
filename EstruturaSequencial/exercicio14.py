pesopeixes = float(input('Informe qual peso dos peixes:'))
pesopermitido = 50
excesso = pesopeixes - 50
multa = excesso * 4
if pesopeixes <= 50:
  print("Não houve excesso de peso:")
else:
  print('Houve excesso de peso de:',excesso,'KG e o valor à ser pago de multa é de R$=', multa)