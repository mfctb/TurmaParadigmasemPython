try:
  letra = str (input("Digite uma Letra ")).upper()
  if letra == ("A") or letra == ("E") or letra ==  ("I") or letra ==  ("O") or letra ==  ("U"):
    print("A LETRA DIGITADA É UMA VOGAL")
  else:
    print("A LETRA DIGITADA É UMA CONSOANTE")
except:
  print("Digite uma letra,vogal ou consoante!")