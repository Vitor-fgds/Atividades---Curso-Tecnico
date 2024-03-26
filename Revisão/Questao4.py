print('================= Cálculo de peso ideal ====================')
altura = float(input('Digite sua altura em metros: '))
sexo = (input('Digite seu sexo [M/F]: ')).upper().replace(' ','')[0]
while True:
  if sexo != 'M' and sexo != 'F':
    print('Digite uma opção válida [M/N]!')
    sexo = (input('Digite seu sexo [M/F]: ')).upper().replace(' ','')[0]
  else:
    break

if sexo == 'M':
  peso_ideal = (72.7*altura) - 58
  print(f'O seu peso ideal é: {peso_ideal::.2f} KG')
elif sexo == 'F':
  peso_ideal = (61.1*altura) - 44.7
  print(f'O seu peso ideal é: {peso_ideal:.2f} KG')

print('=====================================================================')