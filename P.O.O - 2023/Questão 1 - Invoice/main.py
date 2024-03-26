from invoice import Invoice

inv = Invoice(123, 'caneta', 2, 4.5)
inv2 = Invoice(124, 'lapis', 4, 2.5)

print(inv.desc_item)
print(inv2.desc_item) 

'''
Invoice.preço = 15
O parâmetro "preço" é criado na classe com o valor 15, e todos os objetos criados recebem esse atributo com o mesmo valor.

inv.preço = 10
Quando erramos o nome do pârametro, o python o cria. Importante destacar que o parâmetro criado é diferente do parâmetro original, e consequentemente os seus valores também. 
'''