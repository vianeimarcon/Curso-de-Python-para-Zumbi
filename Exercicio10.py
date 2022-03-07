cigarros_fumados = float(input('Digite a quantidade de cigarros fumados dia: '))
# anos_fumados = float(input('Digite a quantos anos esta fumando: '))
perda_vida = 10
total_perda = cigarros_fumados * perda_vida
dias_perdidos = total_perda / 1440
print(f'Total de perdas:  {total_perda} minutos')
if (dias_perdidos > 1):
    print(f'Foram perdidos {dias_perdidos:.2f} dias')
else:
    print(f'Foram perdidos {dias_perdidos:.2f} dia')
cigarros = int(input('Cigarros dia: '))
anos = int(input('Anos fumados: '))
total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print (f'Você perdeu {dias:.1f} dias')
