import os
import time
t = 2
try:

  while True:
    print("====Selecione a Malha:=====")
    print("1 - CACHARREL             |") 
    print("2 - HELANQUINHA           |") 
    print("3 - PP                    |")
    print("4 - PV                    |")
    print("5 - HELANCA               |")
    print("6 - PIQUET                |")
    print("7 - RIBANA                |")
    print("8 - SUPLEX                |")
    print("9 - PV ESTAMPADO          |")
    print("===========================")
    operacao = input("Opção: ")
    if operacao == '1':
      print("cacharrel")
    elif operacao == '2':
      print("helanquinha")
    
    time.sleep(t)
    os.system('clear')
    
    cacharrel = 4.5
    helanquinha = 5.5
    pp = 2.5
    pv = 2.5
    helanca = 2
    piquet = 2.5
    ribana = 3.5
    estampado = 3.5
    suplex = 3.5
    
    if operacao in ('1', '2','3','4','5','6','7','8','9'):
        cacharrel = float(input(f"Digite Quantos Metros Precisa de ?: {operacao}"))
        
        if operacao == '1':
            cacharrel = cacharrel / 4.5
            print(f"Você precisará de: {cacharrel:.2f} kilos de cacharrel")

        elif operacao == '2':
            cacharrel = cacharrel / 5.5
            print(f"Você precisará de: {helanquinha:.2f} kilos de helanquinha")

        elif operacao == '1':
            cacharrel = cacharrel / 4.5
            print(f"Você precisará de: {cacharrel:.2f} kilos de cacharrel")

        elif operacao == '4':
            if numero2 == 0:
                print("Não é possível dividir por zero. Tente novamente!")
            else:
               print("opção inválida!")
        break

          
except:
    print ("opção inválida, tente novamente!")


==============================================================
import os
import time
t = 2
try:

  while True:
    print("====Selecione a Malha:=====")
    print("1 - CACHARREL             |") 
    print("2 - HELANQUINHA           |") 
    print("3 - PP                    |")
    print("4 - PV                    |")
    print("5 - HELANCA               |")
    print("6 - PIQUET                |")
    print("7 - RIBANA                |")
    print("8 - SUPLEX                |")
    print("9 - PV ESTAMPADO          |")
    print("===========================")
    
    operacao = input("Opção: ")
    if operacao == '1':
      cac = "cacharrel"
      print("Cacharrel")
    elif operacao == '2':
      hel = "Helanquinha"
      print("Helanquinha")
      hela = "Helanquinha"
    elif operacao == '3':
      print("PP")
    elif operacao == '4':
      print("PV")
    elif operacao == '5':
      print("Helanca")
    elif operacao == '6':
      print("Piquet")
    elif operacao == '7':
      print("Ribana") 
    elif operacao == '8':
      print("Suplex")
    elif operacao == '9':
      print("PV Estampado")  
    
    time.sleep(t)
    os.system('clear')
    
    cacharrel = 4.5
    helanquinha = 5.5
    pp = 2.5
    pv = 2.5
    helanca = 2
    piquet = 2.5
    ribana = 3.5
    estampado = 3.5
    suplex = 3.5
    
      #if operacao in ('1', '2','3','4','5','6','7','8','9'):
    if operacao == '1':
      cacharrel = float(input(f"Digite Quantos Metros de {cac} Precisa: "))
    elif operacao == '2':
      helanquinha = float(input(f"Digite Quantos Metros de {hel} Precisa: "))
                        
                
    if operacao == '0':
            cacharrel = cacharrel / 4.5
            print(f"Você precisará de: {cacharrel:.2f} kilos de cacharrel")

    elif operacao == '2':
            helanquinh = cacharrel / 5.5
            print(f"Você precisará de: {helanquinha:.2f} kilos de helanquinha")

    elif operacao == '5':
            cacharrel = cacharrel / 4.5
            print(f"Você precisará de: {cacharrel:.2f} kilos de cacharrel")

    #elif operacao == '4':
    #if numero2 == 0:
     #           print("Não é possível dividir por zero. Tente novamente!")
      #      else:
       #        print("opção inválida!")
      #break

          
except:
    print ("opção inválida, tente novamente!")
