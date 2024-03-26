'''02) Você é o líder de uma pequena tripulação pirata. E você tem um plano. Com a ajuda da POO, você deseja fazer um sistema bastante eficiente para identificar navios com saque pesado a bordo!
Infelizmente para você, como saber se um navio está cheio de ouro e não de pessoas?
Você começa escrevendo uma classe Navio genérica:
Você tem acesso ao peso total do navio e "tripulação", que representa o número de humanos no navio.
Sempre que seus espiões virem um novo navio entrar no cais, eles criarão um novo objeto de navio com base em suas observações:
Titanic = Ship(15, 10)

Tarefa
Cada membro da tripulação adiciona 1.5 unidades ao peso do navio. Se depois de remover o peso da tripulação, o peso ainda for superior a 20, então vale a pena saquear o navio. Qualquer navio pesando tanto deve ter muito saque!

Adicione o método vale_a_pena() para decidir se o navio vale a pena ser saqueado. 

Por exemplo:Titanic.vale_a_pena() 
False

Boa sorte e que você encontre GOOOLD!
'''

class Navio:
  def __init__(self,peso_total,numero_tripulaçao):
    self._peso_total = peso_total
    self._numero_tripulaçao = numero_tripulaçao
    self._peso_de_saque = (self._peso_total - (1.5 * self._numero_tripulaçao))

  @property
  def peso_total(self):
    return self._peso_total
  @peso_total.setter
  def peso_total(self, novo_peso):
    self._peso_total = novo_peso
    self._peso_de_saque = (self._peso_total - (1.5 * self._numero_tripulaçao))
    
  @property
  def numero_tripulaçao(self):
    return self._numero_tripulaçao
  @numero_tripulaçao.setter
  def numero_tripulaçao(self, novo_numero):
    self._numero_tripulaçao = novo_numero
    self._peso_de_saque = (self._peso_total - (1.5 * self._numero_tripulaçao))

  @property
  def peso_de_saque(self):
    return self._peso_de_saque

  def vale_a_pena(self):
    if self._peso_de_saque > 20:
      return True
    elif self._peso_de_saque < 20:
      return False