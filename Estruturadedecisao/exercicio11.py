try:
    salario = float(input('Qual salário do colaborador: '))

    if (salario <= 280):
        percentual = 20
    elif (salario <= 700):
        percentual = 15
    elif (salario <= 1500):
        percentual = 10
    else:
        percentual = 5

    print('O salario original é: R$ ', salario)
    print('com o percentual de: ',percentual,'%')

    percentual = percentual/100.0
    aumento = percentual * salario
    salariocomaumento = salario + aumento
    
    print('o aumento concedido foi de: R$ ',aumento)
    print('o novo salário é: R$ ', salariocomaumento)
except:
  print('Valor incorreto!')