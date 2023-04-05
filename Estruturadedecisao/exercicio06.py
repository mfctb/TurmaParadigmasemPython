try:
  numero1 = int(input('Primeiro numero: '))
  numero2  = int(input('Segundo numero : '))
    
  maior = numero1
  
  if (numero2 > maior):
      maior = numero2
  if (numero2 > maior):
      maior = numero2     
 
  print(f'O número maior é: {maior} ')

except:
    print("Dados incorretos!,tente novamente!")