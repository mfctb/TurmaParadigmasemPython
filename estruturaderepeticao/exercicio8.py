try:
  lista = []
  while True:
      n = int(input('Digite o número (0 para encerrar): '))
      lista.append(n)  
      if n == 0:
          break
            
  print ('O maior número da lista é: ',max(lista))  
except:
  print('Digite somente números')