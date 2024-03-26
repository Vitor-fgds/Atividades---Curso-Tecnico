from guerreiro import Guerreiro
from mago import Mago
from monstro import Monstro

class Batalha:
  def __init__(self, oponente1, oponente2):
    self._oponente1 = oponente1
    self._oponente2 = oponente2

  def batalha(self):
    while(True):
      #ataque do guerreiro 1
      if (self.escolha_ataque_defesa() == 'a'):
        self._oponente2.sofre_dano(self._oponente1.atacar())
      else:
        self._oponente1.defender()
      if (self.fim_batalha()):
        return "Player 1 venceu a batalha!"
      #ataque do guerreiro 2
      if (self.escolha_ataque_defesa() == 'a'):
        self._oponente1.sofre_dano(self._oponente2.atacar())
      else:
        self._oponente2.defender()
      if (self.fim_batalha()):
        return "Player 2 venceu a batalha!"

  def fim_batalha(self):
    if(self._oponente1.ponto_vida <= 0 or self._oponente2.ponto_vida <= 0):
      return True
    else:
      return False

  def escolha_ataque_defesa(self):
    while (True):
      print('Deseja atacar (a) ou defender (d)?')
      op = input('Digite sua opção [a ou d]: ').lower()
      if op in ['a','d']:
        return op
      else:
        print('Entrada inválida! Digite apenas (a) ou (d)!')
      