try:
  resposta1 = int(input("Telefonou para a vítima? Digite 1 - Sim ou 0 - Não: "))
  resposta2 = int(input("Esteve no local do crime? Digite 1 - Sim ou 0 - Não: "))
  resposta3 = int(input("Mora perto da vítima? Digite 1 - Sim ou 0 - Não: "))
  resposta4 = int(input("Devia para a vítima? Digite 1 - Sim ou 0 - Não: "))
  resposta5 = int(input("Já trabalhou com a vítima? Digite 1 - Sim ou 0 - Não: "))
  
  soma_respostas = resposta1 + resposta2 + resposta3 + resposta4 + resposta5
  if (soma_respostas < 2):
    print("\nInocente")
  elif (soma_respostas == 2):
    print("\nSuspeita")
  elif (3 <= soma_respostas <= 4):
    print("\nCúmplice")
  elif (soma_respostas == 5):
    print("\nAssassino")        
  
except:
  print("Dados inválidos")