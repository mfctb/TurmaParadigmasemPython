try:
  numero1 = int(input('Primeiro numero: '))
  numero2  = int(input('Segundo numero : '))
  numero3 = int(input('Terceiro numero: '))
  
  maior = numero1
  
  if (numero2 > maior):
      maior = numero2
  if (numero3 > maior):
      maior = numero3
     
  menor = numero1
    
  if (numero2 < menor):
      menor = numero2
  if (numero3 < menor):
      menor = numero3
  
  print(f'O número maior é: {maior} e o menor é: {menor}')

except:
    print("Dados incorretos!,tente novamente!")