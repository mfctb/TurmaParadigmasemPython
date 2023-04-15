try:
  salarios = [0] * 10 # cria uma lista com 10 elementos inicializados com 0
  
  while True:
      vendas = float(input("Informe as vendas da semana (ou digite 0 para sair): "))
      if vendas == 0:
          break
  
      salario = 200 + 0.09 * vendas # calcula o salário do vendedor
      posicao = int((salario - 200) // 100) # calcula a posição na lista de contadores
  
      if posicao < 0: # corrige a posição para evitar índices negativos
          posicao = 0
  
      if posicao > 9: # corrige a posição para evitar índices maiores que 9
          posicao = 9
  
      salarios[posicao] += 1 # incrementa o contador na posição correspondente
  
  # imprime os resultados
  print("Salários na faixa de $200 a $299:", salarios[0])
  print("Salários na faixa de $300 a $399:", salarios[1])
  print("Salários na faixa de $400 a $499:", salarios[2])
  print("Salários na faixa de $500 a $599:", salarios[3])
  print("Salários na faixa de $600 a $699:", salarios[4])
  print("Salários na faixa de $700 a $799:", salarios[5])
  print("Salários na faixa de $800 a $899:", salarios[6])
  print("Salários na faixa de $900 a $999:", salarios[7])
  print("Salários de $1000 em diante:", salarios[8])
except:
  print("Dados Inválidos!")