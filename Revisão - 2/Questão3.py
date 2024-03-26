#Urna Eletrônica
print('''             Urna Eletrônica              ''')
print('''Candidatos:
1 - Jair Rodrigues
2 - Carlos Luz
3 - Neves Rocha
4 - Nulo
5 - Branco
6 - Sair
=============================================''')

lista_1 = []
lista_2 = []
lista_3 = []
lista_4 = []
lista_5 = []

while True:
  voto = int(input('Digite o seu voto: '))
  while True:
    if voto < 1 or voto > 6:
      print('Digite um valor válido:')
      voto = int(input('Digite o seu voto: '))
    else:
      break

  if voto == 1:
    lista_1.append(voto)
  elif voto == 2:
    lista_2.append(voto)
  elif voto == 3:
    lista_3.append(voto)
  elif voto == 4:
    lista_4.append(voto)
  elif voto == 5:
    lista_5.append(voto)
  elif voto == 6:
    break

#Contagem dos votos
print(45*'=')
print(f'O candidato Jair Rodrigues teve {len(lista_1)} votos!')
print(45*'=')
print(f'O candidato Carlos Luz teve {len(lista_2)} votos!')
print(45*'=')
print(f'O candidato Neves Rocha teve {len(lista_3)} votos!')
print(45*'=')

#Porcentagem dos votos
soma_votos = (len(lista_1) + len(lista_2) + len(lista_3) + len(lista_4) + len(lista_5))
porcentagem_nulos = (len(lista_4) * 100) / soma_votos
porcentagem_brancos = (len(lista_5) * 100) / soma_votos
print(f'Tivemos um total de {soma_votos} votos')
print(f'{porcentagem_nulos:.2f}% dos votos foram nulos!')
print(f'{porcentagem_brancos:.2f}% dos votos foram brancos!')
print(45*'=')

#Candidato Vencedor
lista_total = [len(lista_1), len(lista_2), len(lista_3)]

if max(lista_total) == len(lista_1):
  if lista_total.count(len(lista_1)) == 1:
    print(f'O candidato Jair Rodrigues obteve a maior quantidade de votos ({len(lista_1)})!')
  else:
    print('Houve empate!')
elif max(lista_total) == len(lista_2):
  if lista_total.count(len(lista_2)) == 1:
    print(f'O candidato Carlos Luz obteve a maior quantidade de votos ({len(lista_2)})!')
  else:
    print('Houve empate!')
elif max(lista_total) == len(lista_3):
  if lista_total.count(len(lista_3)) == 1:
    print(f'O candidato Neves Rocha obteve a maior quantidade de votos ({len(lista_3)})!')
  else:
    print('Houve empate!')
print(45*'=')