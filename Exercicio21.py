peso = float(input('Digite o peso em kg:  '))
if peso < 50:
  multa = 0
  excesso = 0 
  print(f'Multa e Execesso igua a ZERO {multa, excesso}')
elif peso >= 50:
  multa = 4
  excesso = peso - 50
  multa = 4 * (peso - 50)
  print(f'O valor da Multa é R$: {multa}  e Valor do Execesso é: {excesso} Kg')