try:
  produto1 = float(input('Digite o preço do 1º produto: '))
  produto2  = float(input('Digite o preço do 2º produto:'))
  produto3 = float(input('Digite o preço do 3º produto: '))
  
     
  menor = produto1
    
  if (produto2 < menor):
      menor = produto2
  if (produto3 < menor):
      menor = produto3
  
  print(f'O Valor menor é: {menor}')

except:
    print("Dados incorretos!,tente novamente!")