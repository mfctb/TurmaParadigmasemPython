try:
  litros = float(input("Digite quantos litros de combustível você quer abastecer: "))
  combustivel =(input("Digite A para álcool ou G para gasolina: ")).upper()
  preco = 0
  if combustivel == "A" :
      preco = litros * 1.9
      if litros <= 20:
          preco -= 1.9 * litros * 3 / 100
      else:
          preco -= 1.9 * litros * 5 / 100
  elif combustivel == "G" :
      preco = litros * 2.5
      if litros <= 20:
          preco -= 2.5 * litros * 4 / 100
      else:
          preco -= 2.5 * litros * 6 / 100
  print(f"O preço a pagar é R${preco:.2f}")
except:
  print('dados inválidos')