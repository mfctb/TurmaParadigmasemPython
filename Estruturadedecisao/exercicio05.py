try:
  nota1 = float(input("Digite a primeira nota"))
  nota2 = float(input("Digite a segunda nota"))
  
  if (nota1 > 0 and nota1 <= 10) and (nota2 >0 and nota2 <=10):
    media = (nota1 + nota2) /2
    if media >= 7 and media < 10:
      print (f"Aprovado! com média {media}")
    elif media == 10 :
      print ("Aprovado com Distinção")
    else:
      print (f"REPROVADO COM MÉDIA:{media:.2f}")
  else:
    print ("Notas Invalidas!")
except:
  print ("Só é permitido números")