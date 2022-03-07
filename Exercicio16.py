minuto = float(input('Digite minutos gastos:  '))
if minuto < 200:
  tarifa = minuto * 0.20
  print(f'Voce consumiu: {minuto} minutos com um custo de R$: {tarifa :.2f} no mes')  
if minuto >= 200 and minuto <= 400:
  tarifa = minuto * 0.18
  print(f'Voce consumiu: {minuto} minutos com um custo de R$: {tarifa :.2f} no mes')   
if minuto > 400:
  tarifa = minuto * 0.15
  print(f'Voce consumiu: {minuto} minutos com um custo de R$: {tarifa :.2f} no mes') 
