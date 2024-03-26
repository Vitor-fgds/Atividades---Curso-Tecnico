from conta import Conta, Cliente, Data
cliente2 = Cliente('José','Moura','143497598-98')
data = Data(9,10,2023)
conta1 = Conta('123-4',cliente2,120.0,1000.0, data)
conta1.extrato(cliente2, data)
conta1.deposita(50.0)
conta1.extrato(cliente2, data)


print(type(Conta))
print(type(Cliente))
print(type(Data))
