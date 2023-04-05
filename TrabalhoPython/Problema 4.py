try:

  while True:
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    operacao = input("Opção: ")

    if operacao in ('1', '2', '3', '4'):
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = numero1 + numero2
            print(numero1, "+", numero2, "=", resultado)

        elif operacao == '2':
            resultado = numero1 - numero2
            print(numero1, "-", numero2, "=", resultado)

        elif operacao == '3':
            resultado = numero1 * numero2
            print(numero1, "*", numero2, "=", resultado)

        elif operacao == '4':
            if numero2 == 0:
                print("Não é possível dividir por zero. Tente novamente!")
            else:
                resultado = numero1 / numero2
                print(numero1, "/", numero2, "=", resultado)
        break

          
except:
    print ("opção inválida, tente novamente!")
