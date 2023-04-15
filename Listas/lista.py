#exercicio de lista
try:
  lista_nomes = list()
  lista_nomes.append('michael')
  lista_nomes.append('fernandes')
  lista_nomes.append('38')
  print(lista_nomes)
  print('posição de número 2',lista_nomes[2])
  print(type(lista_nomes))
  lista_nomes.remove('michael')
  print(lista_nomes)
  #lista_nomes.insert(8,2)
  print(lista_nomes)
  #ista_nomes.insert(0,-2)
  print(lista_nomes)
  #lista_nomes.insert(1,2+7)
  print(lista_nomes)
  lista_nomes.remove('38')
  print(lista_nomes)
  lista_nomes.sort()
  print(lista_nomes)
  lista_nomes.reverse()
  print(lista_nomes)
except ValueError:
  print('não é possível remover')

try:
  lista_nomes.pop()
  print(lista_nomes)
  lista_nomes.pop(0)
  print(lista_nomes)
  posicao_obj = lista_nomes.index(0)
  print(posicao_obj)
except IndexError:
  print('Posição não encontrada')

