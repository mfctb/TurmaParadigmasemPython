try:
  numero = input("digite um numero menor que 1000 ---> ")
  texto = str(numero)
  numero2 = len(texto)
  
  if numero2 == 3:
      centena = texto[0:1]
      dezena = texto[1:2]
      unidade = texto[2:3]
      print (texto+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades")
  
  if numero2 == 2:
      dezena = numero2[0:1]
      unidade = texto[1:2]
      print (numero2+" = "+dezena+" dezenas, "+unidade+ " unidades")
  
  if numero2 == 1:
      unidade = numero2[0:1]
      print (texto+" = "+unidade+ " unidade")
except:
  print("Digite somente números")