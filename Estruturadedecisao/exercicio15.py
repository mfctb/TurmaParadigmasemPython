try:
  lado1 = float(input('Primeiro lado: '))
  lado2 = float(input('Segundo  lado: '))
  lado3 = float(input('Terceiro lado: '))
      
  if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print('Não é um triangulo')
  elif (lado1 == lado2) and (lado1 == lado3) :
    print('Trinângulo Equilatero')
  elif (lado1==lado2) or (lado1==lado3) or (lado2==lado3):
    print('Trinângulo Isósceles')
  else:
    print('Trinângulo Escaleno')
except:
 print('valor inválido!')