try:
  respostas = list()
  
  print("Responda as seguintes perguntas sobre o crime:")
  respostas.append(input("Telefonou para a vítima? (sim ou não) "))
  respostas.append(input("Esteve no local do crime? (sim ou não) "))
  respostas.append(input("Mora perto da vítima? (sim ou não) "))
  respostas.append(input("Devia para a vítima? (sim ou não) "))
  respostas.append(input("Já trabalhou com a vítima? (sim ou não) "))
  
  num_positivas = respostas.count("sim")
  
  if num_positivas == 5:
      print("Classificação: Assassino")
  elif num_positivas >= 3:
      print("Classificação: Cúmplice")
  elif num_positivas >= 2:
      print("Classificação: Suspeita")
  else:
      print("Classificação: Inocente")
 
except:
  print('Dados Inválidos')