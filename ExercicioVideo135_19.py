lado_a = float(input('Digite um numero: '))
lado_b = float(input('Digite um numero: ')) 
lado_c = float(input('Digite um numero: '))
if lado_a > lado_b + lado_c or lado_b > lado_a + lado_c or lado_a >lado_c + lado_b:
  print('Não é triangulo')
  print('Um dos lados é maior que a soma dos outros dois')  
elif lado_a == lado_b == lado_c:
  print('Triangulo equiatero')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
  print('Triangulo Isóseles')
else:
  print('Triangulo Escaleno')

