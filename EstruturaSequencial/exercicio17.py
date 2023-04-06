try:
  tamanho  =  float (input('Entre com o tamanho da área: ' ))

  litros  =  tamanho  /  6
  latas  =  litros  /  18
  
  if  latas % 18 !=  0 :
    latas  +=  1
  preço  =  latas  *  80
  
  galões  =  litros  /  3.6
  if galões  %  3.6  !=  0 :
    galões  +=  1
    preco2  =  galões  *  25
  
  # mistura de latas e galões
  mistura_lata  =  int ( litros  /  18.0 )
  mistura_galao  =  int (( litros  - ( mistura_lata  *  18 )) /  3.6 )
  
  if  litros  - ( mistura_lata  *  18 ) %  3.6  !=  0 :
      mistura_galao  +=  1
  
  print ( 'Apenas latas de 18 litros: %d'  %  latas , 'preço: %d'  %  preço )
  print ( 'Apenas galões de 3.6 litros: %d'  %  galoes , 'preço: %d'  %  preco2 )
  print ( 'Mistura: %d latas e %d galões = %.2f'  % (mistura_lata , mistura_galao , (( mistura_lata  *  80 ) +        
 (mistura_galao  *  25 ))))
except:
  print('dados incorretos  ')
