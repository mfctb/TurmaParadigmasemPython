try:
    primeiro = float(input('Primeiro numero: '))
    segundo  = float(input('Segundo numero : '))
    terceiro = float(input('Terceiro numero: '))
    
    if(terceiro > segundo):
        ordem = terceiro
        terceiro = segundo
        segundo = ordem

    if(segundo > primeiro):
        ordem = segundo
        segundo = primeiro
        primeiro = ordem

    if(terceiro > segundo):
        ordem = terceiro
        terceiro = segundo
        segundo = ordem

    print('Ordem Decrescente.:',primeiro,'-',segundo,'-',terceiro)
except:
  print("somente número inteiro ou decimal!")