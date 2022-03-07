perc = float(input('Digite Km percorridos: '))
diasAlug = float(input('Dias alugados: '))
custoDia = 60 * diasAlug
custoKM = 15 * perc
preço_total = custoDia + custoKM
print(f' Valor total pago: R$ {preçoTotal:.2f}')