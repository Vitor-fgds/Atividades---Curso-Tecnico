from Navio import Navio

Naviozao = Navio(50,10)
#Vendo o peso de saque
print(Naviozao.peso_de_saque)

#Testando os setters
Naviozao.peso_total = 60
Naviozao.numero_tripulaçao = 20

#Vendo se os setter deram certo e o peso_de_saque alterou
print(Naviozao.peso_de_saque)

#Vendo se o peso_de_saque altera mudando só o peso total
Naviozao.peso_total = 80
print(Naviozao.peso_de_saque)

#Vendo se o peso_de_saque altera mudando só o numero_tripulaçao
Naviozao.numero_tripulaçao = 10
print(Naviozao.peso_de_saque)

#Vendo se o objeto Naviozao vale a pena ser saqueado
print(Naviozao.vale_a_pena())

#Criando um novo obejto Naviozinho e vendo se ele vale a pena ser saqueado
Naviozinho = Navio(25, 7)
print(Naviozinho.vale_a_pena())