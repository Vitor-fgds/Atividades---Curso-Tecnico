from Empregado import Empregado
Empregado1 = Empregado("João","Oliveira",1000.0)
Empregado2 = Empregado("Maria","Santana",-1000.0)
print(f'====EMPREGADO 1====')
print(Empregado1.primeiro_nome)
print(Empregado1.sobrenome)
print(Empregado1.salario_mensal)


print(f'====EMPREGADO 2====')
print(Empregado2.primeiro_nome)
print(Empregado2.sobrenome)
print(Empregado2.salario_mensal)


#Testando os setters
Empregado1.primeiro_nome = "Vitor"
Empregado1.sobrenome = "Rocha"
Empregado1.salario_mensal = 2000

Empregado2.primeiro_nome = "Alyson"
Empregado2.sobrenome = "Tryndade"
Empregado2.salario_mensal = 5000

#Testando se os setter funcionaram
print(f'====EMPREGADO 1====')
print(Empregado1.primeiro_nome)
print(Empregado1.sobrenome)
print(Empregado1.salario_mensal)


print(f'====EMPREGADO 2====')
print(Empregado2.primeiro_nome)
print(Empregado2.sobrenome)
print(Empregado2.salario_mensal)

#Aumento de 10%
print(f'=====AUMENTOS====')
Empregado1.aumento(10)
print(Empregado1.salario_mensal)
Empregado2.aumento(10)
print(Empregado2.salario_mensal)


