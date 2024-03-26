x = int(input('Digite o número inteiro: '))
print(f'Os número impares até {x} são:')
for i in range (1,x+1,2):
  print(i, end=', ')