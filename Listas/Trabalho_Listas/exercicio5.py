try:
  temperaturas = list()
  meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
  
  for indice in range(12):
      temperatura = float(input(f'Digite a temperatura média de {meses[indice]}: '))
      temperaturas.append(temperatura)
  
  media_anual = sum(temperaturas) / len(temperaturas)
  
  print('Temperaturas acima da média anual:')
  for indice in range(12):
      if temperaturas[indice] > media_anual:
          print(f'{meses[indice]}: {temperaturas[indice]}')
 
except ValueError:
  print('Digite somente números')