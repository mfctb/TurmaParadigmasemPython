try:
  nota = float(input("Insira uma nota 0 até 10: "))
  while (nota < 0) or (nota > 10):
    nota = float(input("Digite a nota corretamente\n Tente novamente:"))
  print("Nota válida")
    
except:
  print("Informe somente números!!!")