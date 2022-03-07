preço = float(input('Digite o valor pago: '))
desconto = float(input('Digite o vl desconto rec %: '))
v = preço * desconto / 100
novoPreço = preço - v
print(f'Valor desconto R$: {v:.2f}')
print(f'Preço final R$: {novoPreço:.2f}')
