try:
  notas = list()  
  
  
  for indice in range(4):
      nota = float(input(f"Digite a nota {indice+1}: "))
      notas.append(nota)  
  
  media = sum(notas) / len(notas)  
  
  
  print("Notas: ", notas)
  print(f"Média:  {media:.2f}")
except ValueError:
  print('Digite somente números')