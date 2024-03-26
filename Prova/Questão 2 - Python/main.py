from Datas import Datas


Data1 = Datas(30,9,2000)
#Testando Getters
print(Data1.dia)
print(Data1._mes)
print(Data1.ano)
#Testando Setters e vendo se a verificação deu certo
Data1.dia = 10
Data1.mes = 30
Data1.ano = 2023

print(Data1.dia)
print(Data1.mes)
print(Data1.ano)

Data1.mes = 11
print(Data1.dia)
print(Data1.mes)
print(Data1.ano)

#Testando o toString
print(Data1.toString())

#Testando o avancar_dia
Data1.avançar_dia()
print(Data1.toString())
Data1.dia = 30
Data1.avançar_dia()
print(Data1.toString())
Data1.dia = 30
Data1.mes = 12
Data1.avançar_dia()
print(Data1.toString())

#Testando qual data é menor
Data2 = Datas(30,12,2023)
print(Data1.data_menor(Data1,Data2))