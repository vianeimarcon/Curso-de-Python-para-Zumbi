x = int(input('Digite um numero: '))
n=0
pi4=0.0
k=1
while n <= x:
  pi4 += k/(2*n+1)
  k*=-1
  n+=1

print(pi4*4)

# Exercicio de PI Ten Eduardo