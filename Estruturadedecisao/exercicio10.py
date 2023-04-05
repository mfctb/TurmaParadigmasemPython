turno = str(input('Digite aqui em que turno você estuda: \nM-maturnino, V-vespertino ou N-noturno:\n ').upper())

if turno == 'M':
    print('Bom dia!')

elif turno == 'V':
    print('Boa tarde!')

elif turno == 'N':
    print('Boa noite!')

else:
    print('Valor inválido!')