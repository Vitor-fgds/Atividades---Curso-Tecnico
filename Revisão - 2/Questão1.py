lista = []
while True:
  num = float(input('Digite um valor maior que 0: '))
  while True:
    if num < 0:
      print('Digite um valor válido')
      num = float(input('Digite um valor maior que 0: '))

    elif num == 0:
      break

    else:
      break
  if num == 0:
    break
  
  lista.append(num)

print(f'Foram inseridos {len(lista)} números.')
print(f'A média dos números é {sum(lista)/len(lista):.2}')