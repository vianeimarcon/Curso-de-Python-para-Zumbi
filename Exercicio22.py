num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))
num3 = float(input('Digite um numero: '))
if num1 >= num2 or num1 >= num3:  
  print(f' Maior: {num1}')
elif num2 >= num3:  
  print(f' Maior: {num2}')
# elif num3 >= num1:
else:
  print(f' Maior: {num3}')

  