'''02) Crie uma classe chamada Pessoa com os atributos nome e idade. Em seguida, crie uma classe chamada Funcionario que herde da classe Pessoa e adicione um atributo adicional chamado salario. Crie um método na classe Funcionario chamado calcular_salario_anual() que retorne o salário anual do funcionário (salário * 12). Crie também uma classe chamada Gerente que herde da classe Funcionario e tenha um atributo adicional chamado bonus. Sobrescreva o método calcular_salario_anual() na classe Gerente para incluir o bônus no cálculo do salário anual.'''

class Pessoa:
  def __init__(self, nome, idade):
    self._nome = nome
    self._idade = idade

class Funcionario(Pessoa):
  def __init__(self, nome, idade, salario):
    super().__init__(nome, idade)
    self._salario = salario

  def calcular_salario_anual(self):
    return (self._salario * 12)
    
class Gerente(Funcionario):
  def __init__(self,nome,idade,salario,bonus):
    super().__init__(nome,idade,salario)
    self._bonus = bonus
  def calcular_salario_anual(self):
    return super().calcular_salario_anual() + self._bonus
    
