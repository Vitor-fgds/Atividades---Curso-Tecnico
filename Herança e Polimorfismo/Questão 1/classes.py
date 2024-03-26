'''01) Crie uma classe chamada Pessoa com os atributos nome e idade. Em seguida, crie uma classe chamada Estudante que herde da classe Pessoa e tenha um atributo adicional chamado curso. Adicione um método à classe Estudante chamado exibir_dados() que exiba o nome, idade e curso do estudante.'''

class Pessoa:
  def __init__(self, nome, idade):
    self._nome = nome
    self._idade = idade


class Estudante(Pessoa):
  def __init__(self, nome, idade, curso):
    super().__init__(nome, idade)
    self._curso = curso


  def exibir_dados(self):
    print(f'Nome: {self._nome}')
    print(f'Idade: {self._idade}')
    print(f'Curso: {self._curso}')
    
