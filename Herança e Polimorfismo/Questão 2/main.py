'''02) Crie uma classe chamada Pessoa com os atributos nome e idade. Em seguida, crie uma classe chamada Funcionario que herde da classe Pessoa e adicione um atributo adicional chamado salario. Crie um método na classe Funcionario chamado calcular_salario_anual() que retorne o salário anual do funcionário (salário * 12). Crie também uma classe chamada Gerente que herde da classe Funcionario e tenha um atributo adicional chamado bonus. Sobrescreva o método calcular_salario_anual() na classe Gerente para incluir o bônus no cálculo do salário anual.'''

from classes import Pessoa, Funcionario, Gerente

Gerente1 = Gerente("Julio", 25, 10000, 12000)

print(Gerente1.calcular_salario_anual())