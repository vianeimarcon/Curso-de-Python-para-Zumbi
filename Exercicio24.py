ganho = float(input('Quanto voce ganha por hora: '))
hora = float(input('Quantas horas trabalhadas: '))
salario_bruto = ganho * hora
print(f'Salario Bruto é: t/ R$ {salario_bruto:.2f}')
imposto_renda = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)
desconto = imposto_renda + inss + sindicato
print(f'Seu total de desconto foi: R$ {desconto:.2f} SENDO Imposto renda foi de: R$ {imposto_renda:.2f} , INSS foi de: R$ {inss:.2f} e Sindicato: R$ {sindicato:.2f}')
print(f'Salario Liquido é: R$ {salario_liquido:.2f}')

# /t = Tabe
# /n = quebra linha