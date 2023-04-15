try:
  login = input("Login: ").upper()
  senha = input("Senha: ").upper()
  
  while login == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")

  print("Cadastro aprovado")

except:
    print("Dados Inválidos!")