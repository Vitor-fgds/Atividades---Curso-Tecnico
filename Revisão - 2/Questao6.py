lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
lista_temperatura = []
teste = 0
for i in range (12):
  x = float(input(f'Digite a temperatura média do mês de {lista_meses[i]} em graus celsius: '))
  lista_temperatura.append(x)

media_anual = sum(lista_temperatura)/12
print(45*'=')
print(f'A média anual de temperatura foi de {media_anual:.2f}° Celsius')
print(45*'=')
print(f'Meses que ultrapassaram a média anual de {media_anual:.2f}° Celsius: ')
for temperatura in lista_temperatura:
  if temperatura > media_anual:
    z = lista_temperatura.index(temperatura,teste,13)
    print(f'{lista_meses[z]} - {temperatura}° Celsius')
    teste += 1
print(45*'=')

 