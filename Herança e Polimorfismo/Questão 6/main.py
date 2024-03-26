from herancas import Pessoa, Gerente, Vendedor, Consultor, Funcionario

gerente = Gerente("Julio", 123, 8000, 1, 4000)
vendedor = Vendedor("Otavio", 132, 3000, 2, 5, 80)
consultor = Consultor("Jorge", 154, 4000, 3 , 150, 15)

print(gerente.calcular_salario())
print(vendedor.calcular_salario())
print(consultor.calcular_salario())