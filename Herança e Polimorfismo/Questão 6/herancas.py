import abc
class Pessoa(abc.ABC):
  def __init__(self, nome, rg):
    self._nome = nome
    self._rg = rg

  def cadastrar(self):
    return "Pessoa Cadastrada"

class Funcionario(Pessoa):
  def __init__(self, nome, rg, salario, registro):
    super().__init__(nome,rg)
    self._salario = salario
    self._registro = registro  

  def calcular_salario(self):
    return self._salario

  def cadastrar(self):
    return "Funcionário Cadastrado"

  def demitir(self):
    return "Funcionário Demitido"


class Vendedor(Funcionario):
  def __init__(self, nome, rg, salario, registro, comissao, numero_vendas):
    super().__init__(nome, rg, salario, registro)
    self._comissao = comissao
    self._numero_vendas = numero_vendas

  def calcular_salario(self):
    self._salario += (self._numero_vendas * self._comissao)
    return self._salario

class Consultor(Funcionario):
  def __init__(self, nome, rg, salario, registro, valor_hora, horas_trabalhadas):
    super().__init__(nome, rg, salario,registro)
    self._valor_hora = valor_hora
    self._horas_trabalhadas = horas_trabalhadas

  def calcular_salario(self):
    self._salario += (self._valor_hora * self._horas_trabalhadas)
    return self._salario
    
class Gerente(Funcionario):
  def __init__(self, nome, rg, salario, registro, bonificacao):
    super().__init__(nome,rg,salario,registro)
    self._bonificacao = bonificacao

  def calcular_salario(self):
    self._salario += self._bonificacao
    return self._salario

