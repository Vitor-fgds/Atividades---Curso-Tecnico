lista_respostas1 = ['SIM', 'sim', 'Sim',]
lista_respostas2 = ['NÃO', 'NAO','Não','Nao','não','nao']
lista_interrogatorio = []
while True:
  print(45*'=')
  print('Você telefonou para a vítima? ')
  x = input('Responda com sim ou não: ').upper()
  while True:
    if x in lista_respostas1:
      x == 'SIM'
      lista_interrogatorio.append(x)
      break
    elif x in lista_respostas2:
      x == 'NAO'
      lista_interrogatorio.append(x)
      break
    else:
      print('Responda apenas com sim ou não! ')
      x = input('Responda com sim ou não: ').upper()
  print(45*'=')
  print('Você esteve no local do crime? ')
  y = input('Responda com sim ou não: ').upper()
  
  while True:
    if y in lista_respostas1:
      y == 'SIM'
      lista_interrogatorio.append(y)
      break
    elif y in lista_respostas2:
      y == 'NAO'
      lista_interrogatorio.append(y)
      break
    
    else:
      print('Responda apenas com sim ou não! ')
      y = input('Responda com sim ou não: ').upper()
  print(45*'=')
  print('Você mora perto da vítima? ')
  z = input('Responda com sim ou não: ').upper()
  
  while True:
    if z in lista_respostas1:
      z == 'SIM'
      lista_interrogatorio.append(z)
      break
    elif z in lista_respostas2:
      z == 'NAO'
      lista_interrogatorio.append(z)
      break
    else:
      print('Responda apenas com sim ou não! ')
      z = input('Responda com sim ou não: ').upper()
  print(45*'=')
  print('Você tinha dívidas com a vítima? ')
  h = input('Responda com sim ou não: ').upper()
  
  while True:
    if h in lista_respostas1:
      h == 'SIM'
      lista_interrogatorio.append(h)
      break
    elif h in lista_respostas2:
      h == 'NAO'
      lista_interrogatorio.append(h)
      break
    else:
      print('Responda apenas com sim ou não! ')
      h = input('Responda com sim ou não: ').upper()
  print(45*'=')
  print('Você já trabalhou com a vítima? ')
  p = input('Responda com sim ou não: ').upper()
  
  while True:
    if p in lista_respostas1:
      p == 'SIM'
      lista_interrogatorio.append(p)
      break
    elif p in lista_respostas2:
      p == 'NAO'
      lista_interrogatorio.append(p)
      break
    else:
      print('Responda apenas com sim ou não! ')
      p = input('Responda com sim ou não: ').upper()
  break

julgamento = lista_interrogatorio.count('SIM')

if julgamento == 2:
  print(45*'=')
  print('Arquivado como suspeito!')
elif julgamento == 3 or julgamento == 4:
  print(45*'=')
  print('Arquivado como cúmplice!')
elif julgamento == 5:
  print(45*'=')
  print('Arquivado como assassino(a)!')
else:
  print(45*'=')
  print('Arquivado como inocente!')