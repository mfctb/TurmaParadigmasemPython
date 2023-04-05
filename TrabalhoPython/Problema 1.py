try:
  idade = int(input("Informe sua idade:"))
   
  if idade >= 16:
    print(f"Tem idade suficiente para votar!") 
  else:
    print(f"Nao tem idade suficiente para votar!")
except:
    print ("Informe corretamente os dados!")
