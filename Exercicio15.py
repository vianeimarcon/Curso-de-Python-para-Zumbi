velocidade = int(input('Digite a velocidade:  '))
if velocidade > 110:
  print('Você será multado')
  multa = 5 * (velocidade - 110)
  print(f'O valor da multa é R$: {multa:.2f}')
else:
  print('Você não foi multado')

  