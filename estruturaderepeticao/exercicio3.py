try:
  nome = input("Digite o seu nome,ele deve ter mais que 3 caracteres: ")
  while len(nome) <= 3:
    nome = input("Qual seu nome [minimo 4 caracteres]: ")  
  idade = int(input("Sua idade: "))
  while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))

  salario = float(input("Salário: "))  
  while (salario<=0):
    salario = float(input(" digite corretamente o seu salário: "))
  sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ").upper()   
  while (sexo!= 'F') and (sexo!='M'):
    sexo = input("Digite corretamente preenchendo somente com 'f' ou 'm': ").upper()
  civil = input("Estado civil (s, c, v ou d): ").upper()
  while (civil!= 'S')and(civil!= 'C')and(civil!= 'V')and(civil!= 'D'):
    civil = input("Deve ser s, c, v ou d: ").upper()
except:
  print('Digite Corretamente o que se pede!')