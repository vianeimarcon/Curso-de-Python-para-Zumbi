salario = float(input('Digite o vl salario: '))
aumento = float(input('Digite o vl do aumento rec %: '))
calculo = salario*aumento/100
salario += calculo

print(f'vl seu aumento R$: {calculo:.2f}')

print(f'Salario atualizado R$: {salario:.2f}')

