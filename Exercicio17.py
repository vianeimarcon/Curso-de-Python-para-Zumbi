minuto = int(input('Digite os minutos gastos: '))
if minuto < 200:
  preço = 0.20
else:
  if minuto <= 400 :
    preço = 0.18
  else:
    preço = 0.15

print(f'Voce consumiu: {minuto} minutos com um custo de R$: {minuto*preço:.2f} no mes')
  