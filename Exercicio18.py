minuto = int(input('Digite os minutos gastos: '))
if minuto < 200:
  preço = 0.20
elif minuto <= 400:
  preço = 0.18
elif minuto <= 800:
  preço = 0.15
else:
  preço = 0.08

print(f'Voce consumiu: {minuto} minutos com um custo de R$: {minuto*preço:.2f} no mes')