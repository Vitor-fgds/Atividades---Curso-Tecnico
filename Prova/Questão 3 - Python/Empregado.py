class Empregado:
  def __init__(self,primeiro_nome,sobrenome,salario_mensal):
    self._primeiro_nome = primeiro_nome
    self._sobrenome = sobrenome
    if salario_mensal > 0:
      self._salario_mensal = salario_mensal
    else:
      print(f'Salário mensal de {self._primeiro_nome} {self._sobrenome} foi declarado menor ou igual a zero, portanto será definido como 0.0')
      self._salario_mensal = 0.0

  @property
  def primeiro_nome(self):
    return self._primeiro_nome

  @primeiro_nome.setter
  def primeiro_nome(self, novo_nome):
    self._primeiro_nome = novo_nome

  @property
  def sobrenome(self):
    return self._sobrenome

  @sobrenome.setter
  def sobrenome(self, novo_sobrenome):
    self._sobrenome = novo_sobrenome

  @property
  def salario_mensal(self):
    return self._salario_mensal

  @salario_mensal.setter
  def salario_mensal(self, novo_salario):
    if novo_salario > 0:
      self._salario_mensal = novo_salario
    else:
      self._salario_mensal = 0

  def aumento(self,porcentagem):
    self._salario_mensal += ((porcentagem/100)*self._salario_mensal)
  