
# cobertura = area * 3  # a litro a cadaa 3 metros
# lata = 18          # uma lata tem 18 litros
# custo_lata = 80
# quant_pintada = 18 * 3
# preço = (lata/18) * custo_lata
area = int(input('Digite a quantidade de metros: '))
if area % 54 == 0:
  latas = area / 54
else:
  latas = int(area / 54) + 1
valor = latas * 80
print(f'{latas} latas')
print(f'Voce utilizou uma lata tinta e custa: R$ {valor:.2f}')
