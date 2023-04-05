try:
  numero = int(input("Digite um número inteiro: "))

  if numero % 2 == 0: 
      print(numero, "é par.")
      if numero % 4 == 0:
          print(numero, "é divisível por 4.")
  else:
      print(numero, "é ímpar.")
  
except:
    print ("opção inválida!")
