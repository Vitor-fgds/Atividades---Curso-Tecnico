'''
05) Imagine que você está desenvolvendo um jogo de RPG e precisa implementar um sistema de combate entre diferentes tipos de criaturas. Crie as classes necessárias para representar as criaturas e o sistema de combate, seguindo as especificações abaixo:
Crie uma classe base chamada Criatura com os seguintes atributos:

* nome: uma string que representa o nome da criatura.
* pontos_vida: um valor inteiro que representa os pontos de vida da criatura.
* ataque: um valor inteiro que representa a força de ataque da criatura.
* defesa: um valor inteiro que representa a defesa da criatura.
'''

from batalha import Batalha
from guerreiro import Guerreiro
from mago import Mago
from monstro import Monstro

while(True):
  print(' - OPONENTE 1 -')
  print('Digite o tipo de guerreiro guerreiro que deseja batalhar: ')
  op = input('Guerreiro, Mago ou Monstro: ').lower()
  if op == 'guerreiro':
    oponente1 = Guerreiro('Guerreiro', 800, 200, 500, 1)
    break
    
  elif op == 'mago':
    oponente1 = Mago('Mago', 700, 250, 400, 1)
    break
    
  elif op == 'monstro':
    oponente1 = Monstro('Monstro', 900, 150, 400, 1)
    break
    
  else:
    print('Erro de personagem digitado. Tente novamente.')

while(True):
  print(' - OPONENTE 2 -')
  print('Digite o tipo de guerreiro guerreiro que deseja batalhar: ')
  op = input('Guerreiro, Mago ou Monstro: ').lower()
  if op == 'guerreiro':
    oponente2 = Guerreiro('Guerreiro', 800, 200, 500, 1)
    break
    
  elif op == 'mago':
    oponente2 = Mago('Mago', 700, 250, 400, 1)
    break
    
  elif op == 'monstro':
    oponente2 = Monstro('Monstro', 900, 150, 400, 1)
    break
    
  else:
    print('Erro de personagem digitado. Tente novamente.')


batalha = Batalha(oponente1, oponente2)

print(batalha.batalha())