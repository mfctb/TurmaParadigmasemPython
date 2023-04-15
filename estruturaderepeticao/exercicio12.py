try:
  print('--' *4)
  print('T A B U A D A')
  print('--' *4)
  n = int (input('Digite um numero: '))
  for a in range(1, 11):
      print('{:1} x {:1} = {:1}'.format(n, a, a*n))
except:
  print("Digite somente número")