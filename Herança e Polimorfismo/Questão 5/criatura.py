'''
05) Imagine que você está desenvolvendo um jogo de RPG e precisa implementar um sistema de combate entre diferentes tipos de criaturas. Crie as classes necessárias para representar as criaturas e o sistema de combate, seguindo as especificações abaixo:
Crie uma classe base chamada Criatura com os seguintes atributos:

* nome: uma string que representa o nome da criatura.
* pontos_vida: um valor inteiro que representa os pontos de vida da criatura.
* ataque: um valor inteiro que representa a força de ataque da criatura.
* defesa: um valor inteiro que representa a defesa da criatura.
'''

import abc
class Criatura(abc.ABC):
  def __init__(self, nome, ponto_vida, ataque, defesa):
    self._nome = nome
    
    if ponto_vida < 400:
      self._ponto_vida = 400
    elif ponto_vida > 1000:
      self._ponto_vida = 1000
    else:
      self._ponto_vida = ponto_vida

    if ataque < 50:
      self._ataque = 50
    elif ataque > 200:
      self._ataque = 200
    else:
      self._ataque = ataque

    if defesa > 200:
      self._defesa = 200
    elif defesa < 0:
      self._defesa = 0
    else:
      self._defesa = defesa

  @abc.abstractmethod
  def atacar(self):
    pass

  @abc.abstractmethod
  def defender(self):
    pass

  def sofre_dano(self, dano):
    dano_final = dano - self._defesa
    if dano_final < 0:
      dano_final = 0

    self._ponto_vida -= dano_final

  @property
  def ponto_vida(self):
    return self._ponto_vida
  @ponto_vida.setter
  def ponto_vida(self, novo_ponto_vida):
    self._ponto_vida = novo_ponto_vida
    