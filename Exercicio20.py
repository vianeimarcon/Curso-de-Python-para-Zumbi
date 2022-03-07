# Verificar se o nao é bissexto
#
from calendar import isleap

ano = int(input('Digite o ano: '))
if isleap (ano):
  print ('Bissexto')
else:
  print('Não é um ano bissexto') 