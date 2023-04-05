try:
  nota1 = float(input('Digite a primeira nota: '))
  nota2 = float (input('Digite a segunda nota: '))
      
  media = (nota1 + nota2) /2
  
  
  
  if media >= 9 and media <= 10 :
     print ('A nota da primeira prova: ',nota1)
     print ('A nota da segunda prova: ',nota2)
     print ('——————————')
     print ('Você tirou um A!')
     print ('Sua media é de:',media)
     print ('você foi aprovado!!')
             
         
  elif media >= 7.5 and media < 9 :
    print ('A nota da primeira prova: ',nota1)
    print ('A nota da segunda prova:' ,nota2)
    print ('——————————')
    print ('Você tirou um B!')
    print ('Sua media é de:',media)
    print ('você foi aprovado!!')
       
          
          
  elif media >= 6 and media < 7.5 :
    print ('A nota da primeira prova: ',nota1)
    print ('A nota da segunda prova: ',nota2)
    print ('——————————')
    print ('Você tirou um C!')
    print ('Sua media é de:',media)
    print ('você foi aprovado!!')
        
          
          
  elif media >= 4 and media < 6 :
    print ('A nota da primeira prova: ',nota1)
    print ('A nota da segunda prova: ',nota2)
    print ('——————————')
    print ('Você tirou um D!')
    print ('Sua media é de:',media)
    print ('você foi reprovado!!')
      
          
  elif media < 4 :
    print ('A nota da primeira prova: ',nota1)
    print ('A nota da segunda prova: ',nota2)
    print ('——————————')
    print ('Você tirou um E!')
    print ('Sua media é de:',media)
    print ('você foi reprovado!!')
except:
  print('Valor inválido')