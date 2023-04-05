try:
    valordahora = float(input("Digite quanto você recebe por hora: "))
    horastrabalhadas = float(input("Digite quantas horas você trabalhou esse mês: "))
  
    salariobruto = valordahora * horastrabalhadas
    if salariobruto <= 900:
        descontoir = 0.0
    elif salariobruto <= 1500:
       descontoir = 5
    elif salariobruto <= 2500:
      descontoir = 10
    else:
      descontoir = 20
  
    IR = salariobruto * (descontoir / 100)
    INSS = salariobruto * (10 / 100)
    FGTS = salariobruto * (11 / 100)
    totaldedescontos = IR + INSS
    salarioliquido = salariobruto - totaldedescontos
  
    print(f"\nSalário Bruto     : R${salariobruto:.2f}",
      f"\n(-) IR (5%)       : R${IR:.2f}",
      f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
      f"\nFGTS (11%)        : R${FGTS:.2f}",
      f"\nTotal de descontos: R${totaldedescontos:.2f}",
      f"\nSalário Liquido   : R${salarioliquido:.2f}",
  )
except:
  print('Valor incorreto!')