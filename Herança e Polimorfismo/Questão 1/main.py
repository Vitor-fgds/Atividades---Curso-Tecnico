'''01) Crie uma classe chamada Pessoa com os atributos nome e idade. Em seguida, crie uma classe chamada Estudante que herde da classe Pessoa e tenha um atributo adicional chamado curso. Adicione um método à classe Estudante chamado exibir_dados() que exiba o nome, idade e curso do estudante.'''

from classes import Pessoa, Estudante

Alexandre = Estudante("Alexandre", 18, "Informática")
Alexandre.exibir_dados()
  